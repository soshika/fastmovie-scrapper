# -*- coding: utf-8 -*-
from selenium import webdriver
import wget
import os
import siaskynet as skynet
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime


proxies = {
   'http': 'http://188.93.64.242:4153',
}

def create_driver(can_download=False):
    PROXY = '188.93.64.242:4153'
    options = Options()
    options.add_argument('--proxy-server=%s' % PROXY)
    options.headless = True
    if can_download:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList",2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir","/root/fastmovie/downloads/")
        #Example:profile.set_preference("browser.download.dir", "C:\Tutorial\down")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
        driver = webdriver.Firefox(firefox_profile=profile, options=options)
        return driver

    driver = webdriver.Firefox(options=options)

    return driver

if __name__ == "__main__":

    for page in range(1, 293):

        driver = create_driver()
        print("Page {0}".format(page) + ('-'*60))
        
        url = 'https://digimovie.li/'

        if page > 1 : 
            url += 'page/{0}/'.format(page)

        print(url)
        driver.get(url)

        movies = driver.find_elements_by_xpath("//h2[@class='lato_font iranYekanReg']")

        for movie in movies:
            link = movie.find_element_by_tag_name('a').get_attribute('href')
            print(link)

            page_driver = create_driver(True)
            page_driver.get(link)
            download_data = page_driver.find_elements_by_xpath("//a[@class='btn_row btn_dl']")
            
            for download in download_data:
                download_file = download.get_attribute('href')
                print('download is about to start at {0} : {1}'.format(datetime.now(), download_file))
                # wget.download(download_file, 'movie.mp4')
                os.system('curl -x \'https://91.106.67.22:9812\' -O {0}'.format(download_file))


            page_driver.quit()

            # download_data = soup_link.find_all('div', class_='btn_row_dl')

            # ind = 1
            # for item in download_data:
            #     a = item.find('a', class_='btn_row btn_dl')['href']
            #     if '480' in a:

            #         print('link no {0}: {1} '.format(ind, a))
            #         download_url = str(a)
            #         print('download is about to start : {0}'.format(download_url))
            #         r = requests.get(download_url)
            #         movie_name = download_url.split('/')[-1].replace('DigiMoviez', 'fastMovie')
            #         with open(movie_name, 'wb') as f:
            #             f.write(r.content)

            #         print('File {0} Downloaded Successfully'.format(movie_name))

            #         directory = directory = os.getcwd()
            #         file_path = directory + '/' + movie_name
                    
            #         client = skynet.SkynetClient() # link to skynet
            #         skylink = client.upload_file(file_path)
            #         print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))

            #         os.remove(file_path)
            #         print("File {0} deleted from server successfully".format(movie_name))
            #         #https://siasky.net/EAAATkfooqnDL-xjmleOf-gwXXLXIsFCWz74hJtxKk-i0Q
            #     ind +=1
            #     print('*'*50)     
        driver.close()       