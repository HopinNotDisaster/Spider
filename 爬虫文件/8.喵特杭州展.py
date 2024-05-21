import requests
import lxml
from lxml import etree

url = 'https://www.nyato.com/manzhan/p330000?p=1'

res = requests.get(url=url)

# print(res.text)
html_tree = etree.HTML(res.text)
titles = html_tree.xpath(
    '//*[@id="body-bg"]/div[4]/div[1]/div[2]/ul/li/div[2]/div[1]/a')
for title in titles:
    print(title.text)
# print(len(titles))