# -*- coding: utf-8 -*-
import os
import siaskynet as skynet
from telethon import TelegramClient, sync
import movieDB
#import logging

api_id=1587025
api_hash='3ad4a744593f7759ca277eb9041643f5'

#logging.basicConfig(level=logging.DEBUG)

client = TelegramClient('FastMovie.onlineSession', api_id, api_hash,
    # You may want to use proxy to connect to Telegram
    #proxy=(socks.SOCKS5, 'PROXYHOST', PORT, 'PROXYUSERNAME', 'PROXYPASSWORD')
)

async def main():
    async for message in client.iter_messages('@Filimo_Pagee'):
        print(message.id, message.text)

        cnt = 0

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.media:
            if '480' or '720' or '1080' in message.text:
                cnt += 1
                path = await message.download_media()
                directory = directory = os.getcwd()
                file_path = directory + '/' + path

                print('File saved to', file_path)

                # link to skynet
                skylink_client = skynet.SkynetClient() 
                skylink = skylink_client.upload_file(file_path)
                print("File {0} Uploaded successfully: link is {1} ".format(path, skylink))

                # remove from server
                os.remove(file_path)
                print("File {0} deleted from server successfully".format(file_path))

                movieDB.InserTableFilimo(skylink, message.text)

        print('-'*50)
    

    # async for message in client.iter_messages('@Filimo_Pagee'):
   

with client:
    client.loop.run_until_complete(main())