# -- coding: utf-8 --
from audioop import add
import pymysql
import os, sys

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
    sql = "select * from info  where carPlateNum = '%s'" % carPlateNum
    cursor.execute(sql)

    tmp = cursor.fetchone()
    # print(cursor.fetc)
    if tmp:
        print('车牌号：', tmp[0])
        print('车主：', tmp[1])
        print('身份证号：', tmp[2])
        print('未处理的违章记录：', tmp[3])
    else:
        print("未查询到记录")


def addRecord(carPlateNum, driverName, driverId, records):
    sql = "insert into info(carPlateNum, driverName,driverID, records)"
    sql2 = sql + "values ('%s' , '%s', '%s', '%s')" % (carPlateNum, driverName, driverId, records)
    cursor.execute(sql2)
    db.commit()


def showInfo():
    sql = "select * from info"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    # print(cursor.fetc)
    print('-----------------------------')
    if tmp:
        for x in tmp:
            print('| 车牌号：', x[0])
            print('| 车主', x[1])
            print('| 身份证号', x[2])
            print('| 未处理违章', x[3])
            print('-----------------------------')

    else:
        print("未查询到记录")


def deleteRecord(carPlateNum):
    # sql = "delete from info where driverName = ('%s')" %(name)
    # sql = "delete from info where records = '1'"
    sql = "delete from info where carPlateNum = '%s'" % (carPlateNum)
    # input = [1]
    cursor.execute(sql)
    db.commit()


menu = """
        主菜单
    ————————————————
        1. 查询
        2. 显示
        3. 删除
        4. 修改
        q. 退出
    ————————————————
"""
running = True

menu_dict = {
    "1": "Command 1",
    "2": "Command 2",
    "3": "Command 3",
    "4": "Command 4",
}


def commands(args):
    command = menu_dict.get(args)
    return command


if __name__ == '__main__':
    # database('浙A67E8F')
    # addRecord('川B8A569','龙秀英','7998134187080011X','1')
    # showInfo()
    # deleteRecord(carPlateNum = '川B8A569')
    print(menu)
    while running:
        cmd = input()
        if cmd != 'q':
            if commands(cmd) is not None:
                if cmd == '1':
                    print('Command 1')
                elif cmd == '2':
                    print('Command 2')
                elif cmd == '3':
                    print('Command 3')
                elif cmd is '4':
                    print('Command 4')
            else:
                print('Unknown Command')
        else:
            print('Exiting......')
            sys.exit()
