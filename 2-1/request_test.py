# http메서드 사용하기

import requests

r1 = requests.get("http://api.aoikujira.com/time/get.php")

text = r1.text
print(text)

binary = r1.content
print(binary)

r2 = requests.get("https://i.ytimg.com/vi/C_rxZ11DKzg/maxresdefault.jpg")

with open("kara.jpg", "wb") as f:
    f.write(r2.content)
print("saved")