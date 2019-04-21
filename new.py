import requests

res = requests.get("http://solelinks.com/api/releases?page=1&upcoming=true")
stocks = res.json()['data']['data']
for item in stocks:
    print(item['id'], end=" ")
    print(item['title'], end=" ")
    print(item['release_date'], end=" ")
    print(item['favouriteCount'])
