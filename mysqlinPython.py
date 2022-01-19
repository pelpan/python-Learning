import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Pqq12138",
    database="carInfo"
)
# 创建一个游标对象
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)
# # 输出数据库
# mycursor.execute("CREATE DATABASE carInfo")  # 创建一个数据库

# 创建数据表
# mycursor.execute("CREATE TABLE sites (carBrand VARCHAR(255) , carPlateNum VARCHAR(255))")

# 查看数据表
'''mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)'''

# 给sites表添加一个主键
# mycursor.execute('ALTER TABLE sites ADD COLUMN id AUTOINCREMENT PRIMARY KEY')

# 插入数据

# 输出表内数据
'''mycursor.execute("SELECT * FROM sites ")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)'''

# 输出指定字段的数据

'''mycursor.execute("SELECT carBrand, carPlateNum FROM sites")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)'''

# 向表中插入一条记录

'''val = ('赣EZ6782', '廖秀英', '330282198801010011', '0')
mycursor.execute("INSERT INTO info(carPlateNum, driverName, driverID, records) VALUES(%s, %s, %s, %s)", val)

mydb.commit()

print(mycursor.rowcount, "SUCCESS")  # 输出行号码'''

# 插入多条数据
# val = ('川B8A569', '龙秀英', '7998134187080011X', '1')
#
# mycursor.execute("INSERT INTO info(carPlateNum, driverName, driverID, records) VALUES(%s, %s, %s, %s)", val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "SUCCESS")  # 输出行号码

# mycursor.execute("SELECT * FROM info WHERE carPlateNum='浙B67E8A'") # 查询指定数据
# sql = "UPDATE info SET records = '1' WHERE carPlateNum = '浙B67E8A'"   # 通过UPDATE更新数据信息
# sql = "DELETE FROM info WHERE carPlateNum = '浙B67E8A'"   # 通过UPDATE更新数据信息
mycursor.execute(sql)
mydb.commit()
myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)