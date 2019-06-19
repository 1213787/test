import requests

url = "https://api.douban.com/v2/movie/top250"

querystring = {"start":"0","count":"10","apikey":"0b2bdeda43b5688921839c8ecb20399b"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "398954ae-983a-43fc-a754-77e85d925b13"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

