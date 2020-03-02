# BeautifulSoup를 이용한 웹 정보 추출 코드

# html의 id로 요소를 찾는 방법

from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1 id="title">스크래핑이란?</h1>
            <p id="body1">웹 페이지를 분석하는 것</p>
            <p id="body2">원하는 부분을 추출하는 것</p>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body1 = soup.find(id = "body1")
body2 = soup.find(id = "body2")

print("#title = " + title.string)
print("#body1 = " + body1.string)
print("#body2 = " + body2.string)