# Python MySQL

## 使用 mysql.connecter 驱动

### 创建数据库连接

```python
import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="yourusername",    # 数据库用户名
  passwd="yourpassword"   # 数据库密码
)
 
print(mydb)
```

### 创建数据库

创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库：

### demo_mysql_test.py:

```python
import mysql.connector  
mydb = mysql.connector.connect(  host="localhost",  user="root",  passwd="123456" )  
mycursor = mydb.cursor()  
mycursor.execute("CREATE DATABASE runoob_db")
```





创建数据库前我们也可以使用 "SHOW DATABASES" 语句来查看数据库是否存在：

### demo_mysql_test.py:

输出所有数据库列表：

```python
import mysql.connector 
mydb = mysql.connector.connect(  host="localhost",  user="root",  passwd="123456" )  
mycursor = mydb.cursor()  
mycursor.execute("SHOW DATABASES")  
	for x in mycursor:  
    print(x)
```



或者我们可以直接连接数据库，如果数据库不存在，会输出错误信息：

### demo_mysql_test.py:

```python
import mysql.connector  
mydb = mysql.connector.connect(  host="localhost",  user="root",  passwd="123456",  database="runoob_db" )
```

