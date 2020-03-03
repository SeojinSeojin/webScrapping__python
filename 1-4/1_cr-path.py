# 링크 안에 있는 대상을 한꺼번에 다운받기 위한 코드

# urllib.parse.urljoin() -> 상대 경로를 절대 경로로 변환

from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print(urljoin(base, "b.html"))
print(urljoin(base, "../index.html"))
# urljoin은 base를 기반으로 상대 경로를 절대 경로로 반환

print(urljoin(base, "http://otherExample.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))
# 상대 경로가 http://, //로 시작 -> base를 무시하고 두번째 매개변수의 url값 리턴
