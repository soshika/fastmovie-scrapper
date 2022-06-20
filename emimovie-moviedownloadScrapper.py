
import requests
import wget
import os
import siaskynet as skynet
from bs4 import BeautifulSoup
import movieDB

if __name__ == "__main__":
    
    

    for page in range(1, 50):
        url = 'https://emimovie.com/category/foreign-movie'
        if page > 1:
            url = url + '/page/{0}'.format(page)
        
        print('Page {0} is about to start'.format(page))

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        movie_links = soup.find_all('div', class_='post-title d-flex float-right w-100')

        for movie in movie_links:
            print('open new page : ', movie.find('a')['href'])
            link = movie.find('a')['href']
            
            dl_response = requests.get(link)
            dl_soap = BeautifulSoup(dl_response.content, 'html.parser')

            all_p_tags = dl_soap.find_all('p', style='text-align: center;')

            for p in all_p_tags:
                final_dl_link = p.find('a')['href']
                if '480' in final_dl_link:
                    print('movie is about to download')
                    movie_name = wget.download(final_dl_link)
                    print('File {0} Downloaded Successfully'.format(movie_name))

                    # get current directory
                    directory = os.getcwd()
                    file_path = directory + '/' + movie_name

                    # link to skynet
                    client = skynet.SkynetClient() 
                    skylink = client.upload_file(file_path)
                    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))

                    # remove file
                    os.remove(file_path)
                    print("File {0} deleted from server successfully".format(movie_name))

                    movieDB.InsertTableEmi(skylink, link)
                    print("Inserted into DB Successfully")
                    print('-'*50)