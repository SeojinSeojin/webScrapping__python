# BeautifulSoup를 이용한 웹 정보 추출 코드

# 네이버 금융에서 환율 정보 추출하기

from bs4 import BeautifulSoup

import urllib.request

url = "https://finance.naver.com/marketindex/"
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
