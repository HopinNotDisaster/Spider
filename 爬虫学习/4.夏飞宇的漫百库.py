import time

import requests
from lxml import etree

# url = 'https://www.manhuabaiku.com/custom/hot'
# res = requests.get(url=url)
# # print(res.text)
# #
# html_tree = etree.HTML(res.text)
# # titles = html_tree.xpath(
# #     '/html/body/div[3]/div/div[3]/div[2]/ul/li[3]/a')
# # for title in titles:
# #     print(title.text)
# # # print(len(titles))
#
# # authors = html_tree.xpath(
# #     '/html/body/div[3]/div/div[3]/div[2]/ul/li[4]/span[1]')
# # for author in authors:
# #     print(author.text)
# # # print(len(titles))
#
# # statuses = html_tree.xpath(
# #     '/html/body/div[3]/div/div[3]/div[2]/ul/li[4]/span[2]/span[2]')
# # for status in statuses:
# #     stas = status.xpath('./a')
# #     for sta in stas:
# #         print(sta.text)
# # print(len(titles))
#
# imgs = html_tree.xpath(
#     '/html/body/div[3]/div/div[3]/div[2]/ul/li[2]/a/img')
# for img in imgs:
#     # print(img)
#     img_link = img.attrib.get('src')
#     print(img_link)
#     img_res = requests.get(url=img_link)
#     img_name = img_link[10:-4].replace('/', '_').replace('.', '-')
#     print(img_name)
#     # print(res.content)
#     with open(f'../RESULT/MBK/{img_name}.jpg', 'wb') as f:
#         f.write(img_res.content)
#     time.sleep(2)
#     # print(len(titles))
#     # break

url = 'https://imgone.pictureorg.com/images/3/1015/45559b26d71afc647ede7b1281c22f77.jpg'
res = requests.get(url=url)
print(res.content)
with open('../RESULT/MBK/1.jpg','wb') as f:
    f.write(res.content)
