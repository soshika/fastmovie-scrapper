
import requests
import wget
from bs4 import BeautifulSoup

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
                    ans = wget.download(final_dl_link)
                    print(ans)