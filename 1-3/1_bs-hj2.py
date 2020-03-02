# CSS 선택자로 요소 뽑기

from bs4 import BeautifulSoup

import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%ED%99%A9%EC%A7%80%EC%9A%B0"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

a_list = soup.select(".mw-parser-output > ul:nth-child(10) > li")

for a in a_list:
    name = a.string
    print("-", name)
