import datetime
import requests
import re



# 只爬取15页
# 一页有20张图片，我要十张！
# 共150张！！

page = 0
while page < 15:
    page += 1
    print(f"正在爬取第{page}页，共15页")

    """
    第一页的url与其他页的url不一样！
    第一页的图片详情url与其他页不一样！
    """

    if page == 1:
        url = "https://pic.netbian.com/index.html"
    else:
        url = f"https://pic.netbian.com/index_{page}.html"
    # url = "https://pic.netbian.com/index.html"

    res = requests.get(url)
    res = res.content.decode("GBK")
    # print(res)
    res = re.findall(r'<ul class="clearfix">(.*?)</div>', res, re.S)[0]
    # print(res)

    if page == 1:
        pic_detail_links = re.findall(r'<a href="(.*?)" title=', res, re.S)
        # print(pic_detail_links)
    else:
        pic_detail_links = re.findall(r'<a href="(.*?)" target=', res, re.S)
        # print(pic_detail_links)

    pic_detail_links = pic_detail_links[:10]
    for i in range(len(pic_detail_links)):
        print(f"正在爬取第{page}页，共15页。第{i + 1}张壁纸，共10张！")
        res_pic_detail = requests.get(f"https://pic.netbian.com{pic_detail_links[i]}")
        res_pic_detail = res_pic_detail.content.decode("GBK")
        # print(res_pic_detail)
        # title = re.findall(r'<title>(.*?)_彼岸图网pic.netbian.com</title>', res_pic_detail, re.S)
        # print(title)
        image_link = re.findall(
            r'v class="photo-pic"><a href="" id="img"><img src="(.*?)" data-pic=".*?" alt=".*?" title',
            res_pic_detail, re.S)[0]
        # # 数据库中的image的值与media下方的图片名字一样
        image = image_link.replace("/", "_")    # 很好的习惯！
        # # print(image)
        image_link = "https://pic.netbian.com/" + image_link
        print(image_link)
        b_img = requests.get(image_link)
        b_img = b_img.content
        print(b_img)


        # 图片的内容  二进制     b_img= \dfgfd\dfb\df\g\d\\dfhdf
        # 图片的名字  str        image    =“str.jpg”  ！！！！
        # 图片的链接             image_link=    “蓝色的链接”


        # 1.存本地   随时随地
        # 2.存数据库 必须拥有（横向的）所有的内容

        with open(f"./RESULT/Second_ShoreImage/{image}", "wb") as f:
            f.write(b_img)

        category = re.findall(r'<p>分类 <span> <a target="_blank" href=".*?">(.*?)</a> </span> </p>', res_pic_detail,
                              re.S)[0]
        print(category)
    #     break
    # #
    # break

