import _csv
import sqlite3
values=[]
id=[]
conn = sqlite3.connect('csvtest.sqlite')
cur = conn.cursor()
with open('customer.csv',mode='r') as csv_file:
    csv_reader = _csv.reader(csv_file)
    for i in csv_reader:
        value = i
        values.append(value)
    id.append(values[0])
cur.execute('DROP TABLE IF EXISTS csvtest')
for j in range(len(id[0])):
    cur.execute('''
    CREATE TABLE "csvtest"(
        "id[0][j]" TEXT,
    ''')
    sql="INSERT INTO csvtest(id[0][j]) VALUES (%s)"
    cur.executemany(sql,values)
    conn.commit()

