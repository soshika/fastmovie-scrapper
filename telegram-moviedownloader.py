# -*- coding: utf-8 -*-
from telethon import TelegramClient, sync
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
                print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())