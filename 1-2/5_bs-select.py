# BeautifulSoup를 이용한 웹 정보 추출 코드

# select(), select_one() -> CSS 선택자를 지정해서 원하는 요소 추출

from bs4 import BeautifulSoup

html = """
<html><body>
    <div id="divid">
        <h1>개강연기..</h1>
        <ul class="items">
            <li>멋사 어쩌지..?</li>
            <li>4월 6일까지 뭐하지..?</li>
            <li>으어어어어어어ㅜㅜㅜ</li>
        </ul>
    </div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#divid > h1").string
print("h1 = ", h1)

li_list = soup.select("div#divid > ul.items > li")
for li in li_list:
    print("li = ", li.string)