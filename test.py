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
# #import logging

# api_id=1587025
# api_hash='3ad4a744593f7759ca277eb9041643f5'

# #logging.basicConfig(level=logging.DEBUG)

# client = TelegramClient('FastMovie.onlineSession', api_id, api_hash,
#     # You may want to use proxy to connect to Telegram
#     #proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
# )

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


   
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({"headless": True})
    [page] = await browser.pages()

    # normally, you go to a live site...
    #await page.goto("http://www.example.com")
    # but for this example, just set the HTML directly:
    await page.setContent("""
    <body>
    <script>
    // inject content dynamically with JS, not part of the static HTML!
    document.body.innerHTML = `<p>hello world</p>`; 
    </script>
    </body>
    """)
    print(await page.content()) # shows that the `<p>` was inserted

    # evaluate a JS expression in browser context and scrape the data
    expr = "document.querySelector('p').textContent"
    print(await page.evaluate(expr, force_expr=True)) # => hello world

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())