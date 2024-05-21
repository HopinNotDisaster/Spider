import re

import requests

url = 'https://github.com/search?q=Python%E5%AD%A6%E4%B9%A0100%E5%A4%A9&type=repositories'
res = requests.get(url=url)
# print(dir(res))
# print(res)
# print(res.text)
# datas = res.json()['payload']['results']

link_titles = re.findall(r'"hl_name":"(.*?)","hl_trunc_description":"(.*?)"', res.text)
for link_title in link_titles:
    link = link_title[0]
    title = link_title[1].replace("<em>", "").replace("</em>", "").replace(" ", "")
    # link_title[1] = link_title[1].replace("<em>", "").replace("</em>", ""))
    link = 'https://github.com/' + link
    print(link, title, len(title))
    link_res = requests.get(url=link)
    link_res = link_res.text
    # print(link_res)
    link_res = re.findall(r'<script type="application/json" data-target="re(.*?)"templateDirectorySuggestion', link_res)
    # link_res = re.findall(r'OrgOwned":true},"currentUser":null,"refInfo":(.*?)]', link_res)
    link_res = link_res[0][437:-2]
    link_res = link_res[164:]
    # ac = '{"name":"master","listCacheKey":"v0:1616209617.029024","canEdit":false,"refType":"branch","currentOid":"4e75007195aa4cdbcb899aeb06b9b08996a4606c"},"tree":{"items":['
    # print(len(ac))
    print(link_res)
    name = re.findall(r'"name":(.*?),"path":".*?","contentType":"directory"}', link_res)
    print(name)
    break
