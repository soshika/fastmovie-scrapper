#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import siaskynet as skynet
import json
import requests
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

    print(response_dic['body'])
    print('-'*40)

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
    print(files)

    subtitles = []
    for file in files:
        data = {'file_id': file['file']}
        subtitle_link = subtitle_download(data)
        print(subtitle_link)
        if subtitle_link == "" or 'https' not in subtitle_link:
            print("Subtitle API is Limited ... ")
        print(subtitle_link)
        subtitle_file = download_linkII(subtitle_link)
        print(subtitle_file)
        subtitle_skylink = upload_to_siasky(subtitle_file)
        print('subtitle is now vtt : ' ,subtitle_skylink)
        subtitles.append({'link': subtitle_skylink, 'language': file['language']})

    ret = ' '.join([str(elem) for elem in subtitles])
    print(ret)
    return ret


if __name__ == "__main__":

    link = 'https://eu.cdn.cloudam.cc/download/2/7/825041/877639/487065/46.105.134.229/1662877006/308c39ba8047337562373bbe958d6cfe80794aef83/series/the_resort/The_Resort_S01E01_480p_WEB-DL_RMTeam_30NAMA.mkv'
    cnama_link = 'https://30nama.com/series/487065/The-Resort-2022'

    get_subtitles(link, cnama_link, '')
