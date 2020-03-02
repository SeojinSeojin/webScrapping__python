# 파이썬의 urllib 패키지의 request 모듈을 이용한 웹상의 파일 다운로드 코드

# urlopen() 사용 -> url의 리소스를 열고
# read() 메소드 -> 데이터를 읽어들임

# open()함수로 파일을 엶
# wb모드 : w-쓰기 모드 + b-바이너리 모드
# write() 메소드 -> 다운로드한 바이너리 데이터를 파일에 저장

import urllib.request

url = "https://image.news1.kr/system/ap/2013/8/28/578546"
savename = "kara.jpg"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("save completed!")