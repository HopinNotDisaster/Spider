import requests
from lxml import etree

url = 'https://www.yoojia.com/rank/6-0-0-0-0-0.html?from_src=hao123_tab_newcar'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie':
        'CITY=%7B%22code%22%3A%22131%22%2C%22name%22%3A%22%E5%8C%97%E4%BA%AC%22%7D; BAIDUID=F204309201F9C66369C941E7D1BBACE5:FG=1; CITY=%7B%22name%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22code%22%3A%22131%22%7D; Hm_lvt_3d2ca9e65ec4a450b97f705740dc51b5=1715859163; Hm_lvt_74dc9c641a3e6ae783a2ad1b67e90643=1715859163; Hm_lpvt_3d2ca9e65ec4a450b97f705740dc51b5=1715859196; Hm_lpvt_74dc9c641a3e6ae783a2ad1b67e90643=1715859196'
    , 'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

res = requests.get(url=url, headers=headers)
res = res.text
html_tree = etree.HTML(res)
# print(html_tree)

infos = html_tree.xpath("//div[contains(@class, 'ranks')]/a")
# students = students[2]
for info in infos:
    name = info.xpath(".//span[@class='info-name']/text()")
    print(name)
    img_link = info.xpath(".//img")[0]
    img_link = img_link.attrib.get('src')
    print(img_link)
