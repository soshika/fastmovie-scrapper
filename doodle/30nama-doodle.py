
import requests
import json

if __name__ == "__main__":
    # rows = movieDB.selectTable()
    #

    links = [


        {
            'url': 'https://eu.cdn.cloudam.cc/download/2/3/825041/826843/4615/144.76.216.58/1669050438/301d30d497740bdfe4b5d68ebfd72f55b0922ccdb7/movies/c/Chicken_Run_2000_720p_BrRip_30nama_30NAMA.mkv',
            'title': 'https://30nama.com/movie/4615/Chicken-Run-2000',
            'new_title': 'https://30nama.com/movie/4615/Chicken-Run-2000'
        },
       
       {
            'url': 'https://eu.cdn.cloudam.cc/download/2/6/825041/441443/9048/144.76.216.58/1669050427/304742c49b0db6ea8c0716197cef427d057f0c0581/movies/m/Monsters_University_2013_720p_BrRip_30nama_30NAMA.mkv',
            'title': 'https://30nama.com/movie/9048/Monsters-University-2013',
            'new_title': 'https://30nama.com/movie/9048/Monsters-University-2013'
        },

        {
            'url': 'https://eu.cdn.cloudam.cc/download/2/3/825041/157164/2085/144.76.216.58/1669050415/302875b6cb393d9946e31382f7a22e26d365136d6e/movies/r/Robin_Hood_1973_1080p_BrRip_YIFY_30NAMA.mp4',
            'title': 'https://30nama.com/movie/2085/Robin-Hood-1973',
            'new_title': 'https://30nama.com/movie/2085/Robin-Hood-1973'
        },

        {
            'url': 'https://eu.cdn.cloudam.cc/download/2/3/825041/341050/235091/144.76.216.58/1669050404/306dd9768a213dbeaff8b6f000369d1fb086a4eb1f/movies/s/Scoob_2020_720p_BrRip_YIFY_30NAMA.mp4',
            'title': 'https://30nama.com/movie/235091/Scoob-2020',
            'new_title': 'https://30nama.com/movie/235091/Scoob-2020'
        },
       
       {
            'url': 'https://eu.cdn.cloudam.cc/download/2/6/825041/390199/137906/144.76.216.58/1669050394/303f2188bd34b6b26ecd02fb0e3b6b0a603974b693/movies/i/Isle_of_Dogs_2018_720p_BrRip_30nama_30NAMA.mkv',
            'title': 'https://30nama.com/movie/137906/Isle-of-Dogs-2018',
            'new_title': 'https://30nama.com/movie/137906/Isle-of-Dogs-2018'
        },

        {
            'url': 'https://eu.cdn.cloudam.cc/download/2/2/825041/459398/9487/144.76.216.58/1669050385/30b842b3108cfc39bd2e2bac33d60f62af55747dbf/movies/h/How_to_Train_Your_Dragon_2_2014_720p_BrRip_30nama_30NAMA.mkv',
            'title': 'https://30nama.com/movie/9487/How-to-Train-Your-Dragon-2-2014',
            'new_title': 'https://30nama.com/movie/9487/How-to-Train-Your-Dragon-2-2014'
        },
        
      
    ]


    for link_data in links :
        link = link_data['url']
        title = link_data['title']
        new_title = link_data['new_title'].split('/')[-1].strip()
        url = 'http://fastmovie.online:9093/doodle/add-link'

        payload = json.dumps({
            "url": link,
            "title": title,
            "new_title": new_title
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        print('-'*50)

