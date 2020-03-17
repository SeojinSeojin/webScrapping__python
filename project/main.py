import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

length = 5
lang = "C언어"
oj_url = "https://www.acmicpc.net/problem/2941"
base_url = "https://search.naver.com/search.naver?where=webkr&sm=mtv_jum&ie-utf8&query="

def make_question_id(oj_url):
    q_id = oj_url.split("/")[-1]
    return q_id

def make_search_url(q_id, lang) :
    search_url = base_url + "백준+" + q_id +"번+"+lang
    return search_url

def make_target_url(search_url):
    result = requests.get(search_url)
    soup = BeautifulSoup(result.text, "html.parser")
    target_url_list = []
    target_url_a = soup.find("div", {"class":"sp_website section"}).find("ul").find_all("a", {"class":"title_link"})
    for target in target_url_a :
        target_url_list.append(target.get("href"))
    print(target_url_list)
    
q_id = make_question_id(oj_url)
search_url = make_search_url(q_id, lang)
print(search_url)
make_target_url(search_url)