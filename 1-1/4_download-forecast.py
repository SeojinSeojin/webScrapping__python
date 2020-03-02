# 파이썬의 urllib 패키지의 request 모듈을 이용한 웹상의 정보 다운로드 코드

# urllib.parse모듈의 urlencode() 함수 -> 요청 전용 매개변수 생성

import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId' : '109'
} # 서울/경기도의 지역번호인 109를 stnId에 대입. 딕셔너리 형태
params = urllib.parse.urlencode(values)
url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()

text = data.decode("utf-8")
print(text)