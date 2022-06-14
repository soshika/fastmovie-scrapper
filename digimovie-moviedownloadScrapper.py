# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys
import importlib
import siaskynet as skynet

if __name__ == "__main__":

    proxy = {
        # "http": 'http://5.161.100.145:1080',
        'http': 'http://81.16.122.116:5678',
    }

    for page in range(1, 293):
        print("Page {0}".format(page) + ('-'*60))
        
        url = 'https://digimovie.li/'

        if page > 1 : 
            url += 'page/{0}/'.format(page)

        print(url)
        response = requests.get(url, proxies=proxy)

        soup = BeautifulSoup(response.content, 'html.parser')

        movies = soup.find_all('h2',class_="lato_font iranYekanReg")

        for movie in movies:
            link = movie.find('a')['href']
            print(link)
            response_link = requests.get(link, proxies=proxy)
            soup_link = BeautifulSoup(response_link.content, 'html.parser')
            download_data = soup_link.find_all('div', class_='btn_row_dl')

            ind = 1
            for item in download_data:
                a = item.find('a', class_='btn_row btn_dl')['href']
                if '480' in a:

                    print('link no {0}: {1} '.format(ind, a))
                    download_url = str(a)
                    print('download is about to start : {0}'.format(download_url))
                    r = requests.get(download_url, proxies=proxy)
                    movie_name = download_url.split('/')[-1].replace('DigiMoviez', 'fastMovie')
                    with open(movie_name, 'wb') as f:
                        f.write(r.content)

                    print('File {0} Downloaded Successfully'.format(movie_name))

                    directory = directory = os.getcwd()
                    file_path = directory + '/' + movie_name
                    
                    client = skynet.SkynetClient() # link to skynet
                    skylink = client.upload_file(file_path)
                    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))

                    os.remove(file_path)
                    print("File {0} deleted from server successfully".format(movie_name))
                    #https://siasky.net/EAAATkfooqnDL-xjmleOf-gwXXLXIsFCWz74hJtxKk-i0Q
                ind +=1
                print('*'*50)            