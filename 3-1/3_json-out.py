# json.dumps() 함수를 이용해 json형식으로 출력하기

import json

kara = {
    "debut" : "2007-03-29",
    "members" : {
        "gyuri" : "leader",
        "seung-yeon" : "lead-vocal",
        "hara" : ["serve-vocal", "main-dancer"],
        "nicole" : ["main-rapper", "main-dancer"],
        "ji-yeoung" : ["serve-vocal"]
    }
}

s = json.dumps(kara)
print(s)