import re
import requests

url = 'https://auto.8891.com.tw/usedauto-newSearch.html?b=28&page=1&api=6.4&device_id=aaea530b-b595-b6a1-e3aa-db0cf3a470bc-a'

headers = {
    'Cookie':
        'uuid=aaea530b-b595-b6a1-e3aa-db0cf3a470bc-a; device_id=aaea530b-b595-b6a1-e3aa-db0cf3a470bc-a; __ab=b; _gcl_au=1.1.280947271.1715763236; _gid=GA1.3.350899269.1715763236; utp=N1715763240; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22rW7XxSxJCgCbX1dyaUSI%22%7D; _ga=GA1.4.1813439902.1715763236; _gid=GA1.4.350899269.1715763236; _hjSessionUser_3714944=eyJpZCI6ImJlMWE5YjRiLWE2OTAtNTc4Mi05NDNlLWM4ZTRhY2ZhZTcwMCIsImNyZWF0ZWQiOjE3MTU3NjMyNDMxMjksImV4aXN0aW5nIjp0cnVlfQ==; lvl1=default-t8891-online-80; lvl2=http://10.2.143.35:80; g=mobile; PHPSESSID=27a03254e55b4f4e24ed4500ebe16abb; webp=1; user_session=1; __gads=ID=c0b4a5ad152c2c85:T=1715763243:RT=1715822480:S=ALNI_MZGxhXDU5YMDHsuPZkgerAa2vUVRA; __gpi=UID=00000e1e22973775:T=1715763243:RT=1715822480:S=ALNI_MbYY_yKoh5CuTpT7Xtg2WUQxcg-BA; __eoi=ID=ad0e9986d0749043:T=1715763243:RT=1715822480:S=AA-AfjZEHrYt-zVunC4JdAaUKKKL; newcar_version=online; globalPopupAd=2; _hjSession_3714944=eyJpZCI6IjYwODUxYmJhLTk2ZTQtNGFjNC1hYzI0LTIzZTBkN2EwZWZjZiIsImMiOjE3MTU4MjI0OTYwNDksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _=1; uvt=eyJ0cyI6eyJVIjo1OTM3My4yNDE4MjY3NzI2OX0sIm50IjoxNzE1ODIyNjE0LjE4OTk5NDEsIm5wIjoiVSJ9; _gali=lspage; _ga_4YCT4M05RT=GS1.1.1715822474.4.1.1715822714.29.0.0; _ga=GA1.3.1813439902.1715763236; _gat_crossdomain=1'
    , 'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

res = requests.get(url=url, headers=headers)
# print(res)
res = res.json()
res = res['data']['data']
for car in res:
    print("价格：", car['auto_price_tag'].replace("<b>", "").replace("</b>", "").strip(),"款式：", car['title'])

