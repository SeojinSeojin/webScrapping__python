# YAML 사용 기초 코드

import yaml

yaml_str = """
Date : 2020-03-04
PriceList:
    -
        name : "Hot Crispy Chicken Burger"
        price : 4500
        set_price : 6300
    -
        name : "Classic Cheese Burger"
        price : 3900
        set_price : 5800
    -
        name : "Bulgogi Burger"
        price : 3400
        set_price : 5400
    -
        name : "Shrimp Burger"
        price : 3400
        set_price : 5400
"""

data = yaml.load(yaml_str)

for item in data['PriceList'] :
    print(item["name"], " -> ", item["price"])