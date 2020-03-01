# 파이썬의 urllib 패키지의 request 모듈을 이용한 웹상의 정보 다운로드 코드

# sys모듈 -> 명령줄에서 매개변수를 입력받도록..

import sys
import urllib.request
import urllib.parse

if len(sys.argv) <= 1:
    print("USAGE : 5_download-forecast-argv.py <REGION NUMBER>")
    sys.exit()

regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
} # 사용자에게 받은 지역번호를 stnId에 대입
params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()

text = data.decode("utf-8")
print(text)