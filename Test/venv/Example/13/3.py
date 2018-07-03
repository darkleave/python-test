#2. 搜索和处理数据

import sqlite3,sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

#query = 'select * from food where %s' % sys.argv[1]
query = 'select * from food '
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
print(names)

for row in curs.fetchall():
    for pair in zip(names,row):
        print(pair)
        print('%s: %s' % pair)



