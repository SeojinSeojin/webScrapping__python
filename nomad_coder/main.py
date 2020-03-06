import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.jobs/career/SearchJobs/python")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
pagination = indeed_soup.find("div", {"class":"listPagination"})
links = pagination.find_all('a')

pages=[]
for link in links[:-1] :
    pages.append(int(link.string))
max_page = pages[-1]

print(pages)