import requests
from lxml import etree

url = "https://www.gamekee.com/ba/"
res = requests.get(url=url)
res = res.text
# print(res)
html_tree = etree.HTML(res)
# print(html_tree)

students = html_tree.xpath(
    "//div[contains(@class, 'item-wrapper') and contains(@class, 'icon-size-6')]")
students = students[2]
for student in students:
    # print(student)
    name = student.attrib.get("title")
    # print(name)
    img_link = "https:" + student.xpath("./img/@src")[0]
    img_name = name
    print(img_link)
    img_b = requests.get(img_link)
    img_b = img_b.content
    with open(f"../RESULT/Blue_Archive/{img_name}.jpg", "wb") as f:
        f.write(img_b)
