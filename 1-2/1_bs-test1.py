# BeautifulSoup를 이용한 웹 정보 추출 코드

from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>스크래핑이란?</h1>
            <p>웹 페이지를 분석하는 것</p>
            <p>원하는 부분을 추출하는 것</p>
        </body>
    </html>
"""

# BeautifulSoup로 분석할 HTML을 지정하고 BeautifulSoup 인스턴스 생성
# 첫번째 인자 -> 위에서 정의한 html
# 두번째 인자 -> 분석기(parser)의 종류
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)
