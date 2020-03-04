# SQLITE 사용 코드

import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items (name, price) VALUES('Cheese Burger', 3900);
INSERT INTO items (name, price) VALUES('Chicken Burger', 4500);
INSERT INTO items (name, price) VALUES('Cheese Stick', 1000);
""")

conn.commit()

cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

for it in item_list :
    print(it)