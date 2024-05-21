import re

import requests

url = 'https://bbs.nga.cn/read.php?tid=40108564&page=1&rand=703'

headers = {
    'Cookie': 'ngaPassportUid=guest06644a24bc3fd3; Hm_lvt_01c4614f24e14020e036f4c3597aa059=1715774029; Hm_lpvt_01c4614f24e14020e036f4c3597aa059=1715774393; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A%22d%22%2C1%3A1715774692%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-43%2C1%3A1715792445%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1715792445%7D%7D; lastvisit=1715778976; guestJs=1715778976'
}

res = requests.get(url=url, headers=headers)
# print(res.text)
res = res.text

comments = re.findall(r"<span id='postcontent\d' class='postcontent ubbcode'>(.*?)</span>", res, re.S)
for c in comments:
    print(c,"***")
