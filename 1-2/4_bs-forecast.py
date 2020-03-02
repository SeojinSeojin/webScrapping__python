# BeautifulSoup를 이용한 웹 정보 추출 코드

# 1-1의 기상청 수정 -> html의 특정 부분만 추출

from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)