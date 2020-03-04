# dump() 함수를 사용해 파이썬 데이터를 YAML로 출력하는 코드

import yaml

professor = [
    { "name" : "Miryang Kim", "gender" : "female", "lecture" : "컴교개" },
    { "name" : "NAWAP", "gender": "male", "lecture" : "클컴개"},
    { "name" : "Younghak Ahn", "gender" : "male", "lecture" : "기프"}
]

yaml_str = yaml.dump(professor)
print(yaml_str)

data = yaml.load(yaml_str)
for p in data :
    print(p["name"])