import bs4
from bs4 import BeautifulSoup

# 通过features来指定解析器！
soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features="lxml")
print(soup.prettify())

i_tag = soup.find("i")
print(i_tag.text)
