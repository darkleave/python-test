#13.2.1 起步

import sqlite3
#获取连接
conn = sqlite3.connect('somedatabase.db')
#获取游标
curs = conn.cursor()
#游标可用来执行SQL查询。

conn.commit()

conn.close()


def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = 0
    try:
        return float(value)
    except Exception:
        pass
    return 0

conn = sqlite3.connect('food.db')
curs = conn.cursor()
curs.execute('''
drop table food
''')
curs.execute('''
create table food (
id text primary key,
water float '水',
desc text,
desc_big text,
kcal float,
protein float,
fat float,
ash float,
carbs float,
fiber float,
sugar float
)
''')
query = 'insert into food values (?,?,?,?,?,?,?,?,?,?,?)'

for line in open('FOOD_DES.TXT'):
    fields = line.split('^')
    if fields.__len__() < 11:
        continue
    vals = [convert(f) for f in fields[:11]]
    print(vals)
    curs.execute(query,vals)

conn.commit()
conn.close()