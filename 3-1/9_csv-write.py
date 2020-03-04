# 파이썬에서 csv파일을 작성하는 코드

import csv, codecs

with codecs.open("test.csv", "w", "euc_kr") as fp :
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["이름", "종류", "가격"])
    writer.writerow(["불고기 김밥", "김밥", 4800])
    writer.writerow(["철판 제육 덮밥", "덮밥", 7000])
    writer.writerow(["갈비 만두", "만두", 4000])
