# xml 분석을 통해 현재 날씨를 분류하는 코드

from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"
if not os.path.exists(savename) :
    req.urlretrieve(url, savename)

xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')
info = {}
for location in soup.find_all("location") :
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)

for weather in info.keys() :
    print("+", weather)
    for name in info[weather] :
        print("| -", name)