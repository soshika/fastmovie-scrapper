from bs4 import BeautifulSoup
from numpy import info
import requests
import movieDB
from datetime import datetime

if __name__ == "__main__":

    for page in range(1, 2):
        print("Page {0}".format(page) + ('-'*100))
        
        url = 'https://digimovie.city/genre/استندآپ-کمدی/'
        if page > 1 : 
            url += 'page/{0}/'.format(page)

        print(url)
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        titles = soup.find_all('h2',class_="lato_font iranYekanReg")
        movie_infos = soup.find_all('span', class_="res_item")
     
        data = soup.find_all('div', class_='meta_item')

        imdb_rates = soup.find_all('div', class_="rate_num")
        descriptions = soup.find_all('div', class_="plot_text")

        covers = soup.find_all('div', 'inner_cover')        

        infos_ind = 0
        for ind in range(10):
            # for get title 
            title = titles[ind].text
            quality, duration, cast, countries, directors, generes = '', '', '', '', '', ''

            movie_data_ul = data[ind].find('ul')
            movie_data_li = data[ind].find_all('li')

            for li in movie_data_li:
                if li.find('div', class_="bottom_sec_single"):
                   continue

                if li.find('span', class_='lab_item').text == 'کیفیت :':
                    quality = li.find('span', class_='res_item iranYekanReg').text
                elif li.find('span', class_='lab_item').text == 'ژانر :':
                    generes = li.find('span', class_='res_item').text
                elif li.find('span', class_='lab_item').text == 'کارگردان :':
                    directors = li.find('span', class_='res_item').text
                elif li.find('span', class_='lab_item').text == 'ستارگان :':
                    cast = li.find('span', class_='res_item').text
                elif li.find('span', class_='lab_item').text == 'محصول کشور :':
                    countries = li.find('span', class_='res_item').text
                elif li.find('span', class_='lab_item').text == 'زمان :':
                    countries = li.find('span', class_='res_item').text
                
            # for get imdb-rate
            imdb_rate = imdb_rates[ind].text

            #for get description
            
            if data[ind].find('div', class_='plot_text') is None:
                description = ''
            else:
                description = data[ind].find('div', class_='plot_text').text
            
            # for get cover
            cover = covers[ind].find('a', href=True).find('img')['src'] 
            uploaded_by = 1
            date_uploaded = datetime.now()

            movieDB.InsertTable(title, duration, quality, imdb_rate, cover, description, date_uploaded, uploaded_by, countries, directors, cast, generes)