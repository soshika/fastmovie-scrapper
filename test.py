# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://filmgirbot.xyz/?showitem=tt0108778") 
# phone = '09150351090'
# password = 'Saman37'

# 


# entry = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="username"]'))
# entry.send_keys(phone) 

# print('sign-u entry filled')

#//*[@id="main-container"]/section/div[1]/div[2]/form/button
# button = WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[3]/p[6]/a'))
# button.click()

# print("New Page")

# # button2 = WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath('/html/body/main/div/table/tbody/tr[2]/td[1]/a'))
# # button2.click()

# #

# link = driver.find_element_by_link_text('https://dllr.almasnewerstorage.ir/Series/F/Friends/S01/480p%20DVDRip%20UNCUT/Friends.S01E01.480p.DVDRip.UNCUT.vrxuniique.mkv')
# link.click()
# entry = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@id="password"]'))
# entry.send_keys(password) 


# from telethon import TelegramClient, sync
# from telethon import functions, types
# import datetime
# from telethon.tl.functions.messages import GetInlineBotResultsRequest


# #import logging

# api_id=1587025
# api_hash='3ad4a744593f7759ca277eb9041643f5'

# #logging.basicConfig(level=logging.DEBUG)

# # client = TelegramClient('FastMovie.onlineSession', api_id, api_hash,
# #     # You may want to use proxy to connect to Telegram
# #     #proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
# # )

# from telethon.sync import TelegramClient
# from telethon import functions, types

# with TelegramClient("FastMovie.onlineSession", api_id, api_hash) as client:
#     result = client(functions.messages.GetInlineBotResultsRequest(
#         bot='@FileMovieBot',
#         peer='me',
#         query='@Searchimdbbot joker',
#         offset='@Searchimdbbot joker',
#         geo_point=types.InputGeoPoint(
#             lat=7.13,
#             long=7.13,
#             accuracy_radius=42
#         )
#     ))
#     print(result.stringify())

# async def main():
#     async for message in client.iter_messages('@Filimo_Pagee'):
#         print(message.id, message.text)

#         cnt = 0

#         # You can download media from messages, too!
#         # The method will return the path where the file was saved.
#         if message.media:
#             if '480' in message.text:
#                 cnt += 1
#                 path = await message.download_media()
#                 print('File saved to', path)  # printed after download is done

# with client:
#     client.loop.run_until_complete(main())


# import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
# from moviepy.editor import *
# from moviepy.video.tools.subtitles import SubtitlesClip

# generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
# subtitles = SubtitlesClip("1-Pilot.srt", generator)

# video = VideoFileClip("movie.mp4")
# result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

# result.write_videofile("movie1.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

# import os
# import siaskynet as skynet

# if __name__ == "__main__":
#     movie_name = 'lukas.png'
#     directory = directory = os.getcwd()
#     file_path = directory + '/' + movie_name

#     client = skynet.SkynetClient()
#     skylink = client.upload_file(file_path)
#     print("Upload successful, skylink: " + skylink)


   
# import asyncio
# from pyppeteer import launch

# async def main():
#     browser = await launch({"headless": True})
#     [page] = await browser.pages()

#     # normally, you go to a live site...
#     #await page.goto("http://www.example.com")
#     # but for this example, just set the HTML directly:
#     await page.setContent("""
#     <body>
#     <script>
#     // inject content dynamically with JS, not part of the static HTML!
#     document.body.innerHTML = `<p>hello world</p>`; 
#     </script>
#     </body>
#     """)
#     print(await page.content()) # shows that the `<p>` was inserted

#     # evaluate a JS expression in browser context and scrape the data
#     expr = "document.querySelector('p').textContent"
#     print(await page.evaluate(expr, force_expr=True)) # => hello world

#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())


#http://dl7.freeserver.top/www2/film/1401/03/Happening.2021.1080p.BluRay.SoftSub.DigiMoviez.mkv

# url = 'http://dl7.freeserver.top/www2/film/1401/03/Happening.2021.1080p.BluRay.SoftSub.DigiMoviez.mkv'

# print(url.split('/')[-1])

# import requests

# def get_proxy():
#     url = "https://www.proxydocker.com/en/proxylist/api?email=zsaman37@yahoo.com&country=IRAN&city=all&port=all&type=https&anonymity=ELITE&state=all&need=all&format=json"

#     payload={}
#     headers = {
#     'Cookie': 'AWSALB=Q0zb2wUVwOX3+lr0bMgppViA5Y0ivJXlfgyXz8iNmft5CtboAA62r21yDUnYspfhpIFWQTeJgHOIvuJyK33/Jv6EEQomF+kYkC5Ojz0tClpYFjgYYQMyiXdtt3Fv; AWSALBCORS=Q0zb2wUVwOX3+lr0bMgppViA5Y0ivJXlfgyXz8iNmft5CtboAA62r21yDUnYspfhpIFWQTeJgHOIvuJyK33/Jv6EEQomF+kYkC5Ojz0tClpYFjgYYQMyiXdtt3Fv'
#     }

#     response = requests.request("GET", url, headers=headers, data=payload)

#     data = response.json()
#     return data


# proxies_dic = get_proxy()
# proxies = proxies_dic['Proxies']


# for proxy in proxies:
#     print(proxy)

# import wget
# import os
# import requests
# import siaskynet as skynet

# from requests import Request, Session

# url = 'https://eu.cdn.cloudam.cc/download/2/4/825041/829612/338013/46.105.134.229/1656609140/300e9863a92ddf46c7a529170193202eb9bbd57bed/series/birdgirl/Birdgirl_S02E01_480p_WEB-DL_RMTeam_30NAMA.mkv'

# # headers = {'Content-Disposition': 'inline; filename=Friends_S03E03_UNCUT_DVDRip_30NAMA.avi'}
# s = Session()
# req = Request('GET', url)
# prepared = req.prepare()
# # del prepared.headers['Content-Disposition']
# prepared.headers['Content-Disposition'] = 'inline; filename=Birdgirl_S02E01_480p_WEB-DL_RMTeam_30NAMA.mkv'

# response = s.send(prepared)

# # r = requests.get(url, headers=headers)
# with open('test.mkv', 'wb') as f:
#     f.write(response.content)

# print('downloaded')

# directory = os.getcwd()
# file_path = directory + '/' + 'test.mkv'

# client = skynet.SkynetClient() 
# skylink = client.upload_file(file_path)
# print("Uploaded successfully: link is {0} ".format(skylink))


# import zipfile
# with zipfile.ZipFile("joker.zip","r") as zip_ref:
#     zip_ref.extractall("joker-sub")

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print( 'wrong argv: %d' % len(sys.argv))
        sys.exit(0)
    '''$ python srt2vtt.py ./in/mySubtitle.srt ./out/vttFolder/'''
    # parse arg
    print(len(sys.argv))
    in_file_path, out_folder_path = sys.argv[1:3]
    in_file_name = os.path.basename(in_file_path)
    #out_folder_path = sys.argv[2]
    out_file_name = os.path.splitext(in_file_name)[0] + '.vtt' # remove '.srt'

    with open(in_file_path) as in_file:

        # srt open, read, group frames
        frames = in_file.read().split('\n\n')

        # parse frames
        for rowid in range(len(frames)):
            # split frame into three parts: [frameid, timestamp, en]
            frames[rowid] = frames[rowid].split('\n', 2)
            # NOTE frames[rowid][2] may contain nothing (slient frame)

        # discard invalid frame (e.g. silence frame with no line)
        frames = [frame for frame in frames if len(frame) == 3]

        # update frame index
        for index in range(len(frames)):
            frames[index][0] = index + 1

        #open vtt and redirect stdout
        out_file = open(os.path.join(out_folder_path, out_file_name), "w")
        # must UTF-8

        oldstdout = sys.stdout # save original stdout
        sys.stdout = out_file # stdout redirect
        # vtt write
        print( 'WEBVTT\n' ) # vtt file header
        for frame in frames:
            print( frame[0] ) # frame id
            print( frame[1].replace(',', '.') ) # format timestamp
            print("") # for chinese line
            print( "\nNOTE\n" + frame[2] + '\n') # en subtitle
            sys.stdout.flush()

        # close vtt file
        out_file.close() # print() require close() to flush
        sys.stdout = oldstdout; # restore stdout

    print('done: %s' % (out_folder_path + '/' + out_file_name) )