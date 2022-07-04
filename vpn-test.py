import requests

proxy = {
    "http": 'http://46.209.56.112:8080',
}
response=requests.get('https://digimovie.li', proxies=proxy)

print(response.status_code)
