import requests
from lxml import etree

url = "https://y.qq.com/n/ryqq/toplist/26"
res = requests.get(url=url)
res = res.text
# print(res)
html_tree = etree.HTML(res)
# print(html_tree)

titles = html_tree.xpath("//*[@id='app']/div/div[2]/div[2]/div[3]/ul[2]/li/div/div[3]/span/a[2]")
for title in titles:
    print(title)



"""
    其中有个json格式的数据，它里面包含有很多undefined，导致不能进行反序列化！替换掉即可！


"""