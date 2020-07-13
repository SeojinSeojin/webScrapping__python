from bs4 import BeautifulSoup
import urllib.request as req

# 정보 가져오기

url = "http://www.albamon.com/list/gi/mon_gi_tot_list.asp?ps=20&ob=6&lvtype=1&rArea=,I000&rpcd=,9061,9060,&partExc=&rEdu=,30&rWDate=1&Empmnt_Type="
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")


table = soup.select("#subcontent > form > div.gListWrap > table > tbody")[0]
job_list_tr = table.select("tr")

for job in job_list_tr:
    j = job.select("p.cName a")[0]
    job_title = j.string
    job_link = "http://www.albamon.com" + j["href"]

    print(f"이름 : {job_title}")
    print(f"링크 : {job_link}")
