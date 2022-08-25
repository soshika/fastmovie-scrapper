import os
import json
import requests
from numpy import full
import movieDB
import wget
import siaskynet as skynet
import struct
from time import sleep
import urllib.request as ur
import m3u8
import threading

def sky_upload_go(file_path, file_name):
    url = "http://localhost:9092/movies/siasky?file"

    payload={}
    files=[
    ('file',(file_name,open(file_path,'rb'),'video/mp2t'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.json())
    link = response.json()['filepath']
    return link


segments_data = {}

def download_segment(ind, segment):
    try:
        segment_name = wget.download(segment.uri)
        full_path = os.getcwd() + '/' + segment_name
        skylink = sky_upload_go(full_path, segment_name)
        # os.remove(segment_name)
        segments_data [ind] = skylink
    except Exception as err :
        print(err)



def convert_to_m3u8(file_path):
    global segments_data
    segments_data = {}

    threads = []

    playlist = m3u8.load(file_path)  # this could also be an absolute filename

    ind = 0
    for segment in playlist.segments:
        t = threading.Thread(target= download_segment,args=(ind, segment,))
        threads.append(t)
        ind += 1

    for t in threads:
        t.start()
        sleep(0.5)
    
    for t in threads:
        t.join()
       
    for i in range(len(playlist.segments)):
        print('segment {0} is : {1}'.format(i, segments_data[i]))
        segment.uri = segments_data[i]
        
        
    playlist.dump('ffs.m3u8')
    full_path = os.getcwd() + '/' + 'ffs.m3u8'
    client = skynet.SkynetClient() 
    skylink = client.upload_file(full_path)

    return skylink

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

def download_upload(link, file_name, size, quality, subtitle, season, episode):
    print('se {1}- ep {2} download is about start  {0}'.format(file_name, season, episode))
    try:
        movie_name = wget.download(link)
    except Exception as err :
        print(err)
        return 

    print('\nFile {0} Downloaded Successfully'.format(movie_name))

    # get current directory
    directory = os.getcwd()
    file_path = directory + '/' + movie_name

    m3u8_link = convert_to_m3u8(file_path)

    hash = ''
    # hash_err = hashFile(file_path)
    # if hash_err != 'IOError' and hash_err != 'SizeError':
    #     hash = hash_err
    
    # link to skynet
    # client = skynet.SkynetClient() 
    # skylink = client.upload_file(file_path)
    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, m3u8_link))

    # remove file
    os.remove(file_path)
    print("File {0} deleted from server successfully".format(movie_name))

    # quality, subtitle, hash, size
    movieDB.InsertTableCnamaSeries(m3u8_link, file_name, quality, subtitle, hash, size, season, episode)
    print("Inserted into DB Successfully")
    print('-'*50)

if __name__ == "__main__":

    result = []
    
    f = open('json/cnama-series.json')
    data = json.load(f)

    season = 1
    episode = 1

    for _, value in data['result']['list'].items():
        for ep in value:
            for q in ep['file']['source']:
                if q['label'] == '720p':
                    src = ''
                    if 'src' in q:
                        src = q['src']
                    elif '2ch' in q:
                        src = q['2ch']
                    result.append({'episode': episode, 'season':season, 'src': src, 'quality': q['label'], 'subtitles': ep['subtitle']})
            
            episode += 1
        season += 1
        episode = 1

    f.close()

    for ep in result:
        info = ur.urlopen(ep['src'])
        real_size  = int()
        try:
            size = int(info.headers['Content-Length'])/ 1000000000
            print('size of file is : ', size)
            real_size = size
        except Exception as err:
            print(err)

        download_upload(ep['src'], 'https://30nama.com/series/13205/Rick-and-Morty-2013', real_size, ep['quality'], ep['subtitles'], ep['season'], ep['episode'])        
