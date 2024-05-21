import requests
import re

music_list = []
url = 'https://y.qq.com/n/ryqq/singer/003HK9132IEj2d'

headers = {
    'Cookie':
        'RK=l7u9CTGCyc; ptcz=0ae26166dfe82da3fb4608cc6176be7aee20b3ebb54879c480e94fc12ad959a8; logTrackKey=0cffaa3abab544388853f7d8405e65e3; pgv_pvid=3958142811; fqm_pvqid=ca99e86c-5f60-43ea-8035-b3e816e5b830; fqm_sessionid=260a85fd-f295-4478-bb10-4950b1181f6f; pgv_info=ssid=s7518344103; ts_uid=4092871780; _qpsvr_localtk=0.37770514737003635; login_type=1; psrf_qqunionid=08E37A33F066BC203ED963F1AF8E2D0D; music_ignore_pskey=202306271436Hn@vBj; euin=oio57Kc5oi4q7n**; psrf_qqopenid=0EE915D4D69F0E2789213C733BBAEA4D; wxopenid=; qqmusic_key=Q_H_L_63k3NvIu6tz-dTJ9YSpqCwXnxhuNI5dynyuNmbQy2CXmkjW1dOAkX8ZWkRAXPvoyVv4YoRzGsl438RY4; psrf_musickey_createtime=1715656888; tmeLoginType=2; uin=3315813594; psrf_qqrefresh_token=6008FE8E434EC9041AD9D5D6C906B8DF; wxrefresh_token=; wxunionid=; qm_keyst=Q_H_L_63k3NvIu6tz-dTJ9YSpqCwXnxhuNI5dynyuNmbQy2CXmkjW1dOAkX8ZWkRAXPvoyVv4YoRzGsl438RY4; psrf_access_token_expiresAt=1723432888; psrf_qqaccess_token=B30DEFCBAAABE0B99F17C551F9BB1DC0; ts_refer=www.kdocs.cn/; ts_last=y.qq.com/n/ryqq/singer/003HK9132IEj2d'
    ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

res = requests.get(url=url, headers=headers)
res = res.text
# print(res)

res = re.findall(r'<a title="专辑 1" href="/n/ryqq/singer/003HK9132IE(.*?)":"002HgJfp494', res)[0]
# print(res)
# print(type(res))
res = re.findall(
    r'</i>关注 <span>59.6万</span></a></div></div><div st(.*?)她的心中。 ","descstr":"',
    res)
print(res)
# print(type(res))

# https://y.qq.com/n/ryqq/songDetail/004ArOCZ13Lvqo
# mus = re.findall(r'<a title="(.*?)" href="(.*?)">.*?<span class="songlist__song_txt', res, re.S)
# for i in mus:
#     print(i)
# one = re.findall(
#     r'<a title="(.*?)" href="(.*?)">希望有羽毛和翅膀<span class="songlist__song_txt">(.*?)</span></a></span><div class="mod_list_menu"><a class="list_menu__item list_menu__play" title="播放',
#     res.text, re.S)
# # print(len(one[0]))
# print(one[0][0])
