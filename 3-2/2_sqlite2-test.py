# sqlite 더 자세히 알아보기?

# SQL 내부에 삽입할 값을 "?"으로 표현, 두번째 매개변수로 해당 값을 넘겨줌

import sqlite3

filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER)
""")
conn.commit()

cur = conn.cursor()
cur.execute(
    "INSERT INTO items (name, price) VALUES (?, ?)",
    ("Orange", 5200)
)
conn.commit()

cur = conn.cursor()
data = [("Mango", 7700), ("Abocado", 10000)]
cur.executemany(
    "INSERT INTO items(name, price) VALUES (?, ?)", 
    data
)
conn.commit()

cur = conn.cursor()
price_range = (4000, 8000)
cur.execute(
    "SELECT * FROM items WHERE price>=? AND price<=?",
    price_range
)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)