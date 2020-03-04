# Pandas를 이용해 엑셀 파일을 읽기

import pandas as pd

filename = "stats_104102.xlsx"
sheet_name = "stats_104102"
book = pd.read_excel(filename, sheet_name=sheet_name, header=1)

book = book.sort_values(by=2018, ascending=False) #2018년 기준, 오름차손
print(book)