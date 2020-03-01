# 파이썬의 urllib 패키지의 request 모듈을 이용한 웹상의 정보 다운로드 코드

# 2에서 사용했던 urlopen()과 read()메서드

# decode()메서드 -> binary형식의 데이터를 문자열로 변환

import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)