import requests
from string import digits
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import random
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def parse_file(text):
    tmp = text.split('/')[-1]
    x = float(''.join([c for c in tmp if c in digits or c == '.']))
    if x < 20.0:
        x = x * 1000.0
    if x <= 3000:
        return True
    
    return False

def get_proxy():
    url = "https://www.proxydocker.com/en/proxylist/api?email=zsaman37@yahoo.com&country=IRAN&city=all&port=all&type=https&anonymity=ELITE&state=all&need=all&format=json"

    payload={}
    headers = {
    'Cookie': 'AWSALB=Q0zb2wUVwOX3+lr0bMgppViA5Y0ivJXlfgyXz8iNmft5CtboAA62r21yDUnYspfhpIFWQTeJgHOIvuJyK33/Jv6EEQomF+kYkC5Ojz0tClpYFjgYYQMyiXdtt3Fv; AWSALBCORS=Q0zb2wUVwOX3+lr0bMgppViA5Y0ivJXlfgyXz8iNmft5CtboAA62r21yDUnYspfhpIFWQTeJgHOIvuJyK33/Jv6EEQomF+kYkC5Ojz0tClpYFjgYYQMyiXdtt3Fv'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    return data

def create_driver():
    # proxies_dic = get_proxy()
    # proxies = proxies_dic['Proxies']

    # proxy = proxies[random.randint(0, len(proxies))]
    # print("proxy is : ", proxy)

    PROXY = '188.93.64.242:4153'
    options = Options()
    options.add_argument('--proxy-server={0}'.format(PROXY))
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver

if __name__ == "__main__":
    url = 'https://filmgirbot.xyz/'
    
    driver = create_driver()
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="searchinput"]').send_keys('joker')
    driver.implicitly_wait(20)
    link = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div/div[1]/a').get_attribute('href')

    response = requests.get(link)

    soup = BeautifulSoup(response.content, 'html.parser')
    movie_links = soup.find_all('p', class_='text-left direction-ltr')

    print(len(movie_links))

    for movie in movie_links:
        if parse_file(movie.text) and '480' in movie.text:
            download_link = movie.find('a')['href']
            print('download is about to start {0}'.format(download_link))
            driver.get(download_link)
            # cmd = 'curl --tlsv1.2 -x \'http://91.106.64.94:9812\' -O {0}'.format(download_link)
            # print('cmd is : ', cmd)

            # os.system(cmd)

    