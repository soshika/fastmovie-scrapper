from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from movieDB import selectTableEmi

def create_driver():

    # PROXY = '188.93.64.242:4153'
    options = Options()
    # options.add_argument('--proxy-server={0}:{1}'.format(proxy['ip'], proxy['port']) )
    # options.headless = True
    driver = webdriver.Firefox(options=options, executable_path='./geckodriver')

    return driver

if __name__ == "__main__":

    driver = create_driver()

    rows = selectTableEmi()

    for row in rows:
        url = row[2]
        print('login url is : ', url)

        driver.get(url)

        name = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/section/section[1]/section[1]/article/figure/figcaption/main/section/div[1]/h2').text
        print(name)

        director = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/section/section[1]/section[2]/main/div/section[2]/section/section[1]/main/div/section[2]/ul/li[7]/div[2]/p/a').text
        print(director)

        age = driver.find_element(By.XPATH, '//*[@id="main-container main-container-default"]/section/section[1]/section[2]/main/div/section[2]/section/section[1]/main/div/section[2]/ul/li[5]/div[2]/p/a').text
        print(age)

        imdb = driver.find_element(By.XPATH, '//*[@id="single-30nama"]/figure/figcaption/main/section/ul[3]/li[2]/section/a/div[1]/p[1]').text
        print(imdb)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/section/section[1]/section[1]/article/figure/figcaption/main/section/div[2]/div/div[1]/div[2]/div').click()
        sleep(1)
        detail = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/section/section/section[1]/section[1]/article/figure/figcaption/main/section/div[2]/div/div[2]/p').text

        print(detail)

    