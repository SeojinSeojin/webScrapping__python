# BeautifulSoup를 이용한 웹 정보 추출 코드

# find_all() 메서드 -> 파라미터에 해당하는 모든 태그 추출

# attrs속성 -> 링크의 href 속성 추출

from bs4 import BeautifulSoup

html = """
    <html><body>
        <ul>
            <li><a href="https://www.youtube.com/watch?v=zYoYoBtLqOY"> STEP </a></li>
            <li><a href="https://www.youtube.com/watch?v=8Q7FerAVQbw"> Damaged Lady </a></li>
        </ul>
    </body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links : 
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)