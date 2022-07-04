from re import sub
from urllib import response
import movieDB
from selenium import webdriver
import os
import requests
import random
import siaskynet as skynet
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep

# constants

username = 'zsaman37@yahoo.com'
password = 'Saman123456'

def create_driver():

    # PROXY = '188.93.64.242:4153'
    options = Options()
    # options.add_argument('--proxy-server={0}:{1}'.format(proxy['ip'], proxy['port']) )
    # options.headless = True
    driver = webdriver.Firefox(options=options, executable_path='./geckodriver')

    return driver

if __name__ == "__main__":
    driver = create_driver()

    url = 'https://30nama.com/login'
    print('login url is : ', url)

    driver.get(url)
    action = webdriver.ActionChains(driver)

    username_fill = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/main/div[1]/div[2]/div/div/input')
    
    for character in username:
        username_fill.send_keys(character)
        sleep(random.uniform(0.1,0.4))
    
    
    password_fill = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/main/div[1]/div[3]/div/div/input')

    for character in password:
        password_fill.send_keys(character)
        sleep(random.uniform(0.1,0.5))

    print('time to click on submit button')
    sleep(10)

    for page in range(1, 2393):
        url = 'https://30nama.com/movie'
        if page > 1:
            url = url + '?page={0}'.format(page)
        
        driver.get(url)
        #
        for movie in range(1, 25):
            print('page #{1} movie #{0} is about to enter : '.format(movie, page))

            movie_link = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/div/main/div/section/section/div/section[{0}]/div/article/figure/a'.format(movie)).click()
            sleep(3)

            download_url_db = driver.current_url
            db_url = driver.current_url
            print(db_url)
            query = 'SELECT id FROM cnama WHERE `link` LIKE \'%{0}\' ;'.format(db_url.split('/')[-1])
            print(query)
            if movieDB.findFromTableCnama(query):
                driver.back()
                sleep(1)
                continue
            download_url = driver.current_url + '?section=download#download'
            print('download url is : ', download_url)
            driver.get(download_url)
            sleep(3)

            

            for link in range(1, 20):
                try:
                    download_href = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section[2]/main/div/section[2]/section/section/section/div/section[{0}]/section/section/div[2]/div[2]/div/a'.format(link)).get_attribute('href')
                    movieDB.InsertTableCnama(download_href, db_url)
                    print('insert into DB successfully ', download_href)
                except Exception as err:
                    # print(err)
                    break
            
            print('----------------------------------------------------------')
            driver.get(url)

           
