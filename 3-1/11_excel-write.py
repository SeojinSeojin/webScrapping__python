# 파이썬으로 엑셀 파일을 작성하는 코드

import openpyxl

filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)

sheet = book.active

for i in range(0, 9) :
    total = int(sheet[str(chr(i+66))+"3"].value)
    seoul = int(sheet[str(chr(i+66))+"4"].value)
    output = total - seoul
    print("서울 제외 인구 =", output)

    sheet[str(chr(i+66))+"21"] = output
    cell = sheet[str(chr(i+66))+"21"]

    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

filename = "population.xlsx"
book.save(filename)
print("Book File Saved")