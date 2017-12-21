import pymysql

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='a123456',db='mysql')
cur = conn.cursor()
cur.execute("USE test2")
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
