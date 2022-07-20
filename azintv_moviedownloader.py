
import movieDB
import siaskynet as skynet
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def create_driver():

    # PROXY = '188.93.64.242:4153'
    options = Options()
    # options.add_argument('--proxy-server={0}:{1}'.format(proxy['ip'], proxy['port']) )
    # options.headless = True
    driver = webdriver.Firefox(options=options, executable_path='./geckodriver')
    return driver


if __name__ == "__main__":
    driver = create_driver()

    
    

    for page in range(1, 112):
        url = 'https://azintv6.xyz/movie/'
        if page > 1:
            url = url + '/page/{0}/'.format(page)
        
        print('login url is : ', url)
        driver.get(url)

        for movie in range(1, 25):
            link = driver.find_elements(By.XPATH, '//*[@id="new-movies"]/div/div[{0}]/div/div[1]/a'.format(movie)).get_attribute('href')
            print(link)
            print('robot is about to enter to new movie page ')
            # link.click()

            # sleep(3)
            # driver.back()

            data = ''
            'https://dllrrr.nowsaymyname.xyz/Movies/2022/11252248/Dog%202022%201080p%20BluRay%20x264%20AAC5.1%20YIFY.mp4'
            'https://dllrrr.nowsaymyname.xyz/Movies/2022/11252248/Dog%202022%20720p%20BluRay%20x264%20AAC%20YIFY.mp4'

            'https://dllrrr.nowsaymyname.xyz/Movies/2022/1464335/Uncharted%202022%201080p%20BluRay%20x264%20AAC5.1%20YIFY.mp4'

