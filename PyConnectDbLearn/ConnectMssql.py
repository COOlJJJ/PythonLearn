import pymssql

conn = pymssql.connect(host='127.0.0.1', user='user', password='123456', database='Demo')

cur = conn.cursor()

cur.execute('select top 5 * from [dbo].[OEE]')
# 如果update/delete/insert记得要conn.commit()
# 否则数据库事务无法提交
print(cur.fetchall())

cur.close()
conn.close()
