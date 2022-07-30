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
    sleep(20)

    for page in range(1, 371):
        url = 'https://30nama.com/series'
        if page > 1:
            url = url + '?page={0}'.format(page)
        
        driver.get(url)

        for movie in range(1, 25):
            print('page #{1} movie #{0} is about to enter : '.format(movie, page))
            #
            movie_link = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/div/main/div/section/section/div/section[{0}]/div/article/figure/a'.format(movie)).click()
            sleep(3)

            download_url_db = driver.current_url
            download_url = driver.current_url + '?section=download#download'
            print('download url is : ', download_url)
            driver.get(download_url)
            sleep(3)

            for season in range(1, 50):
                try:
                    for link in range(1, 20):
                        try:                              
                            link_href = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section[2]/main/div/section[2]/section/section/section[{1}]/div/section[{0}]/section/section/div[2]/div[2]/div/div'.format(link, season))
                            link_href.click()
                            sleep(3)
                            for episode in range(1, 100):
                                try:
                                    download_href = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section[2]/main/div/section[2]/section/section/section[{2}]/div/section[{0}]/section/section[2]/div/section/ul/li[{1}]/div/a'.format(link, episode, season)).get_attribute('href')
                                    print(download_href)
                                    if '720' in download_href and ('10bit' not in download_href  and '10bt' not in download_href):
                                        print('hereeeeeeeeeeeeeeeeeeeeeeeee')
                                        movieDB.InsertTableCnamaSeries(download_href, download_url_db)
                                        print('insert into DB successfully ', download_href)
                                    sleep(1)
                                except Exception as err:
                                    break
                            
                            link_href.click()
                        except Exception as err:
                            break

                except Exception as err:
                    break

            driver.get(url)
