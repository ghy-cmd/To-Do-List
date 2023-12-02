import sqlite3

db_file = "identifier.sqlite"
conn = sqlite3.connect(db_file)
cur = conn.cursor()
sql = 'INSERT INTO TASK(contend,year,month,day,everyday,title,importance) VALUES(?,?,?,?,?,?,?)'
contend = '这是一个任务'
year = 2022
month = 8
day = 12
everyday = 1
title = '标题'
importance = 1
cur.execute(sql, (contend, year, month, day, everyday, title, importance))
conn.commit()
cur.close()
conn.close()
