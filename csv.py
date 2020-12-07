# read file customers.csv and save into database

import _csv
import sqlite3
values=[]
url='C:/Users/PC/Desktop/Python/csvtest.db'     #paste your path of file.db
conn = sqlite3.connect(url)
cur = conn.cursor()
with open('customers.csv',mode='r') as csv_file:
    csv_reader = _csv.reader(csv_file)
    for i in csv_reader:
        value = i
        values.append(value)
values.remove(values[0])
cur.execute('''CREATE TABLE "csvtest"(
    "customerid" INTEGER,
    "firstname" TEXT,
    "lastname" TEXT,
    "companyname" TEXT,
    "billingaddress1" TEXT,
    "billingaddress2" TEXT,
    "city" TEXT,
    "state" TEXT,
    "postalcode" TEXT,
    "country" TEXT,
    "phonenumber" INTEGER,
    "emailaddress" TEXT,
    "createddate" TEXT )''')
sql="INSERT INTO csvtest(customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city,state , postalcode, country, phonenumber,emailaddress, createddate) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
cur.executemany(sql,values)
conn.commit()
