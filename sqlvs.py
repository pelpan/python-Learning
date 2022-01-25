""" import pymysql
#1连接数据库
conn=pymysql.connect(host='localhost',
port=3306,
user='root',
password='Pqq12138',
db='stockfix',
charset='utf8')
# #2获取游标
cursor = conn.cursor()
# #3执行查询，并获取查询的总行数
rowNums = cursor.execute('SELECT * FROM test1')
# print('查询的行数为' + str(rowNums))
# #4.遍历结果，获取查询的结果cl
ResultList = cursor.fetchall()
for i in range(len(ResultList)): 
    print(ResultList[i])
# #提交如果需要插入语句的时候使用commit#
conn.commit()
# #关闭
cursor.close()
conn.close()  """

import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Pqq12138',
    database='carInfo'
)

cursor = db.cursor()
age = 22
sql = 'delete from test1 where age = %d' %(age)
# cursor.execute('show tables')
# cursor.execute('select * from test1')
cursor.execute(sql)
db.commit()
'''data = cursor.fetchall()
for x in data:
    print(x)'''

db.close()