# 파이썬의 urllib 패키지의 request 모듈을 이용한 웹상의 파일 다운로드 코드

# urlretrieve() 사용 -> 파일을 바로 저장

import urllib.request

url = "https://www.topstarnews.net/news/photo/201802/365826_9377_3543.jpg"
savename = "gyuri.jpg"

urllib.request.urlretrieve(url, savename)
print("save completed!")