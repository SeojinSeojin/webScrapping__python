# 파이썬의 csv 모듈 사용하여 csv 파일 읽기

import codecs, csv

filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "euc_kr") # file pointer

reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader :
    print(cells[1], cells[2])