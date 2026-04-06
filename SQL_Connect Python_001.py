# "__________SQL Connect Python_____"

import pymysql as sql

det = sql.connect(
    host="localhost",
    user="root",
    passwd="livewire"
)
"""conobj = det.cursor()
conobj.execute("create database Reason")"""

data = sql.connect(host="localhost", user="root", passwd="livewire", database="Reason")
cur = data.cursor()

#cur.execute("create table Datadetz(sname varchar(30), rollno int, Sub_name varchar(15))")
cur.execute("insert into Datadetz(sname,rollno,Sub_name) values('Abhi',1001,'Hindi')")
cur.execute("insert into Datadetz(sname,rollno,Sub_name) values('Vinod',1003,'Kanada'),('Harish',1005,'English')")
cur.execute("insert into Datadetz(sname,rollno,Sub_name) values('Hashik',1002,'Tamil')")
cur.execute("select * from Datadetz")
ab = cur.fetchall()
"""for x in ab:
    print(x)"""

cur.execute("update Datadetz set rollno=1004 where sname='Harish'")
cur.execute("insert into Datadetz (sname,rollno,Sub_name) values('Yazh',1005,'German')")
cur.execute("select * from Datadetz")
ac = cur.fetchall()
"""for x in ac:
    print(x)"""

cur.execute("delete from Datadetz where sname='Harish'")
cur.execute("select * from Datadetz")
ae = cur.fetchall()
for y in ae:
    print(y)