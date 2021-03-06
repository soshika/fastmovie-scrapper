import requests
import movieDB
import os
import struct
import json
import wget
import siaskynet as skynet
import urllib.request as ur
import ffmpeg
import re


def get_serie_data(data):
    url = "http://fastmovie.online:9092/movies/data"

    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    response_dic = response.json()
    return response_dic['body']['imdbID']

def subtitle_search(data):
    url = "http://fastmovie.online:9092/subtitles/search"

    payload = json.dumps(data, indent = 4) 
    
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_dic = response.json()
    subtitles = response_dic['body']['data']

    ret = []
    cnt = {}
    for subtitle in subtitles:
        # for file in subtitle['attributes']['files']:
        if subtitle['attributes']['language'] not in cnt:
            cnt[subtitle['attributes']['language']] = 1
            for file in subtitle['attributes']['files']:
                ret.append({'file': file['file_id'], 'language': subtitle['attributes']['language']})
        elif cnt[subtitle['attributes']['language']] == 1:
            cnt[subtitle['attributes']['language']] = 2
            for file in subtitle['attributes']['files']:
                ret.append({'file': file['file_id'], 'language': subtitle['attributes']['language']})
    
    return ret

def subtitle_download(data):
    url = "https://fastmovie.online:9092/subtitles/download"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    response_dic = response.json()

    return response_dic['body']['link']

def parse_title_year(link):
    name = link.split('/')[-1]
    name = name.replace('-', ' ')
    year = name[-4:]
    name = name[:len(name)-4].strip()
    return {'title': name, 'year': int(year)}

def re_finder(pattern):
    ret = re.findall('S([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?', pattern)
    if len(ret) > 0:
        return (str(int(ret[0][0])), str(int(ret[0][1])))
    
    return None

def get_subtitles(download_link ,movie_link, hash):
    data = parse_title_year(movie_link)
    imdb_id = get_serie_data(data)
    se = re_finder(download_link)
    languages = 'en,fa,fr,ru,hi'

    data = {'imdb_id': imdb_id, 'languages': languages, 'season_number': se[0], 'episode_number': se[1]}
    files = subtitle_search(data)

    subtitles = []
    for file in files:
        data = {'file_id': file['file']}
        subtitle_link = subtitle_download(data)
        subtitles.append({'link': subtitle_link, 'language': file['language']})

    return subtitles

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    ffmpeg.input(mkv_file).output(out_name).run()
    print("Finished converting {}".format(mkv_file))
    return out_name

def hashFile(path):
    """Produce a hash for a video file: size + 64bit chksum of the first and
    last 64k (even if they overlap because the file is smaller than 128k)"""
    try:
        longlongformat = 'Q' # unsigned long long little endian
        bytesize = struct.calcsize(longlongformat)
        fmt = "<%d%s" % (65536//bytesize, longlongformat)

        f = open(path, "rb")

        filesize = os.fstat(f.fileno()).st_size
        filehash = filesize

        if filesize < 65536 * 2:
            return "SizeError"

        buf = f.read(65536)
        longlongs = struct.unpack(fmt, buf)
        filehash += sum(longlongs)

        f.seek(-65536, os.SEEK_END) # size is always > 131072
        buf = f.read(65536)
        longlongs = struct.unpack(fmt, buf)
        filehash += sum(longlongs)
        filehash &= 0xFFFFFFFFFFFFFFFF

        f.close()
        returnedhash = "%016x" % filehash
        return returnedhash

    except IOError as err:
        print(err)
        return "IOError"

def download_upload(link, file_name, size, quality):
    print('download is about start  {0}'.format(file_name))
    try:
        movie_name = wget.download(link)
    except Exception as err :
        print(err)
        return 

    print('\nFile {0} Downloaded Successfully'.format(movie_name))

    # get current directory
    directory = os.getcwd()
    file_path = directory + '/' + movie_name

    # convert mkv to mp4
    mp4_file =convert_to_mp4(file_path)
    mp4_file_path = directory + '/' + mp4_file

    # link to skynet
    client = skynet.SkynetClient() 
    skylink = client.upload_file(mp4_file_path)
    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))


    # get hash of file
    hash = hashFile(file_path)
    if hash == 'IOError' or hash == 'SizeError':
        hash = ''

    se = re_finder(link)
    subtitles = get_subtitles(link, file_name, hash)

    # remove mkv file
    os.remove(file_path)
    print("File {0} deleted from server successfully".format(movie_name))

    # remove mp4 file
    os.remove(mp4_file_path)
    print("File {0} deleted from server successfully".format(mp4_file))

    # insert to db
    # (skylink, link, quality, subtitle, hash, size, season, episode)
    movieDB.InsertTableCnamaSeriesSkylink(skylink, file_name, quality, subtitles, hash, size, se[0], se[1])
    print("Inserted into DB Successfully")
    print('-'*50)

if __name__ == "__main__":
   
    dp = dict()
    rows = movieDB.selectSeriesTable()

    for row in rows:
        if '720' in row[1]:
            link = row[1]
            info = ur.urlopen(link)
            try:
                size = int(info.headers['Content-Length'])/ 1000000000
                print('size of file is : ', size)
            except Exception as err:
                print(err)
            
            if size <= 1.0:
                if '720' in info.headers['Content-Disposition'] and '{0}-720'.format(row[2]) not in dp:
                    dp['{0}-720'.format(row[2])] = True
                    quality = '720p-'
                    if 'x265' in row[1]:
                        quality = quality + 'x265-'
                    if '10bit' in row[1]:
                        quality = quality + '10bkt-'
                    if 'BrRip' in row[1]:
                        quality = quality + 'BrRip-'
                    if 'DVDRip' in row[1]:
                        quality = quality + 'DVDRip-'
                    if 'BluRay' in row[1]:
                        quality = quality + 'BluRay-'
                    
                    if quality == '720p-':
                        quality = '720p-webDL'
                    
                    print(link, row[2], size, quality)
                    download_upload(link, row[2], size, quality)
                    movieDB.delete_task(row[0])