# -- coding: utf-8 --
from audioop import add
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Pqq12138',
    database='carInfo',
    # cursorclass = pymysql.cursors.DictCursor # 设置返回值为字典类型
)

# 光标
cursor = db.cursor()


def database(carPlateNum):
    sql = "select * from info  where carPlateNum = '%s'" %carPlateNum
    cursor.execute(sql)

    tmp = cursor.fetchone()
    # print(cursor.fetc)
    if tmp:
        print('车牌号：',tmp[0])
        print('车主：',tmp[1])
        print('身份证号：',tmp[2])
        print('未处理的违章记录：',tmp[3])
    else:
        print("未查询到记录")

def addRecord(carPlateNum, driverName, driverId, records):
    sql = "insert into info(carPlateNum, driverName,driverID, records)" 
    sql2 = sql + "values ('%s' , '%s', '%s', '%s')"%(carPlateNum , driverName , driverId , records)
    cursor.execute(sql2)
    db.commit()

def showInfo():
    sql = "select * from info"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    # print(cursor.fetc)
    if tmp:
        for x in tmp:
            print(x)
    else:
        print("未查询到记录")

def deleteRecord(carPlateNum):
    # sql = "delete from info where driverName = ('%s')" %(name)
    # sql = "delete from info where records = '1'"
    sql = "delete from info where carPlateNum = '%s'" %(carPlateNum)
    # input = [1]
    cursor.execute(sql)
    db.commit()

if __name__ == '__main__':
    # database('浙A67E8F')
    addRecord('川B8A569','龙秀英','7998134187080011X','1')
    # showInfo()
    # deleteRecord(carPlateNum = '川B8A569')
