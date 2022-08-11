import requests
import movieDB
import os
import struct
import json
import wget
import siaskynet as skynet
import urllib.request as ur
import re


def download_linkII(link):
    file_name = 'subtitle.srt'
    response = requests.get(link)
    open("./subtitle.srt", "wb").write(response.content)
    return file_name

def upload_to_siasky(file):
    base = os.getcwd() + '/'
    # base = '/usr/src/app'
    full_path = base + file
    print('full_path of srt subtitle is : ', full_path)
    upload_path = base + '/subtitle.vtt'
    print('upload_path is : ', upload_path)

    lines = open(full_path, "r")

    with open(upload_path, 'a') as f:
        f.write("WEBVTT\n")
    
    for line in lines:
        tmp = line.replace(',', '.')
        with open(upload_path, 'a') as f:
            f.write(tmp)

    client = skynet.SkynetClient() 
    skylink = client.upload_file(upload_path)

    # remove file
    os.remove(full_path)
    os.remove(upload_path)

    return skylink

def get_serie_data(data):
    url = "http://fastmovie.online:9092/movies/data"

    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    response_dic = response.json()
    return response_dic['body']['imdbID']

def subtitle_search(data):
    url = "http://fastmovie.online:9092/subtitles/search"

    payload = json.dumps(data, indent = 4) 
    
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
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
    url = "http://fastmovie.online:9092/subtitles/download"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
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
        if subtitle_link == "" or 'https' not in subtitle_link:
            print("Subtitle API is Limited ... ")
        print(subtitle_link)
        subtitle_file = download_linkII(subtitle_link)
        print(subtitle_file)
        subtitle_skylink = upload_to_siasky(subtitle_file)
        print('subtitle is now vtt : ' ,subtitle_skylink)
        subtitles.append({'link': subtitle_skylink, 'language': file['language']})

    ret = ' '.join([str(elem) for elem in subtitles])
    return ret

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    os.system('ffmpeg -i {0}  -vcodec libx264 -f mp4 {1}'.format(mkv_file, out_name))
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
    print('mp4 file is : ', mp4_file)

    # link to skynet
    client = skynet.SkynetClient() 
    skylink = client.upload_file(mp4_file)
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
    os.remove(mp4_file)
    print("File {0} deleted from server successfully".format(mp4_file))

    print(skylink, file_name, quality, subtitles, hash, size, se[0], se[1])
    movieDB.InsertTableCnamaSeriesSkylink(skylink, file_name, quality, subtitles, hash, size, se[0], se[1])
    print("Inserted into DB Successfully")
    print('-'*50)

if __name__ == "__main__":
   
    dp = dict()
    rows = movieDB.selectSeriesTable()

    for row in rows:
        # if '720' in row[1]:
        link = row[1]
        info = ur.urlopen(link)
        try:
            size = int(info.headers['Content-Length'])/ 1000000000
            print('size of file is : ', size)
        except Exception as err:
            print(err)
        
        if size <= 1.0:
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