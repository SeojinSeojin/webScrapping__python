import requests
from bs4 import BeautifulSoup

LIMIT = 20
INDEED_URL = "https://www.indeed.jobs/career/SearchJobs/python"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class":"listPagination"})
    links = pagination.find_all('a')

    pages=[]
    for link in links[:-1] :
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_page) :
    jobs=[]
    locs=[]
    for page in range(last_page) : 
        result = requests.get(f"{INDEED_URL}?jobOffset={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("h3", {"class":"listSingleColumnItemTitle"})
        for result in results :
            job = result.find("a").string.split("-")[0]
            jobs.append(job)
    return jobs

# 직업 이름, 지역만 추출 가능하다. . indeed 사이트가 바뀌었나보다 ㅜㅜ


def main():
    last_indeed_page = extract_indeed_pages()
    print(extract_indeed_jobs(last_indeed_page))

main()