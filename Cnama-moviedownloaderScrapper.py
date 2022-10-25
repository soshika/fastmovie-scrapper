from urllib import response
import requests
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import requests
import json

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
    movie_download_cnt = 0
    driver = create_driver()

    url = 'https://30nama.com/login'
    print('login url is : ', url)

    driver.get(url)
    action = webdriver.ActionChains(driver)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/section/section[1]/section/main/div[1]/div[1]/div').click()
    sleep(2)

    username_fill = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/main/div[1]/div[2]/div/div/input')
    
    for character in username:
        username_fill.send_keys(character)
        sleep(random.uniform(0.1,0.4))
    
    
    password_fill = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/main/div[1]/div[3]/div/div/input')

    for character in password:
        password_fill.send_keys(character)
        sleep(random.uniform(0.1,0.5))

    print('time to click on submit button')
    sleep(30)

    for page in range(6, 2393):
        if movie_download_cnt == 100:
            break
        url = 'https://30nama.com/movie?sortBy=all&genre=all'
        if page > 1:
            url = url + '&page={0}'.format(page)

        print(url)
        
        driver.get(url)
        #
        for movie in range(1, 25):
            if movie_download_cnt == 100:
                break
            print('movie #{0} is about to enter : '.format(movie))
            movie_link = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section/section/div/main/div/section/section/div/section[{0}]/div/article/figure/a'.format(movie)).click()
            sleep(3)

            download_url_db = driver.current_url
            print(download_url_db)
            download_url = driver.current_url + '?section=download#download'
            print('download url is : ', download_url)
            driver.get(download_url)
            sleep(3)

            for link in range(1, 20):
                try:
                    download_href = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section[2]/main/div/section[2]/section/section/section/div/section[{0}]/section/section/div[2]/div[2]/div/a'.format(link)).get_attribute('href')
                    if '720' in download_href and ('10bit' not in download_href  and '10bt' not in download_href):
                        title = download_url_db
                        new_title = title.split('/')[-1]
                        

                        endpoint_url = "http://fastmovie.online:9093/doodle/add-link"

                        payload = json.dumps({
                            "url": download_href,
                            "title": title,
                            "new_title": new_title
                        })
                        headers = {'Content-Type': 'application/json'}

                        response = requests.request("POST", endpoint_url, headers=headers, data=payload)
                        from pprint import pprint
                        pprint(response.text)
                        movie_download_cnt += 1
                        break
                except Exception as err:
                    # print(err)
                    break
            
            print('-'*50)
            driver.get(url)

           
