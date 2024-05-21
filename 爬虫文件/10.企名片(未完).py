import requests

url = 'https://vipapi.qimingpian.cn/search/recommendedItemList'

data = {
    'page': 2,
    'num': 20,
    'sys': 'vip'
}

res = requests.get(url=url, data=data)
print(res.json())
