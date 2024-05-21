import requests
import lxml
from lxml import etree

url = "http://www.iupian.com/top.html"
res = requests.get(url=url)
res = res.content.decode()
print(res)
html_tree = etree.HTML(res)
# print(html_tree)


movies = html_tree.xpath("//ul[@class='serach-ul']//a")
for movie in movies:
    # print(movie.xpath("./a")[0].attrib.get("title"))
    if movie.attrib.get("title") and len(movie.attrib.get("title"))>2 :
        print(movie.attrib.get("title"))