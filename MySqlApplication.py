# -- coding: utf-8 --
import sys
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Pqq12138',
    database='carInfo'
)

# 光标
cursor = db.cursor()
# 输出格式化
fmt = "{:10}{:15}"

def search(column, data):
    sql = "select * from info  where %s = '%s'" % (column, data)
    cursor.execute(sql)
    tmp = cursor.fetchall()
    if tmp:
        for x in tmp:
            print('--------------------------------')
            print(fmt.format('车牌号：', x[0]))
            print(fmt.format('车主：', x[1]))
            print(fmt.format('身份证号：', x[2]))
            print(fmt.format('未处理的违章记录：', x[3]))
            print('--------------------------------')
    else:
        print("未查询到记录")


def searchInfo():
    while running:
        print(menu3)
        cmd = input()
        if cmd != '0':
            if commands(cmd) is not None:
                if cmd == '1': # 车牌号
                    data = input('请输入车牌号')
                    search('carPlateNum', data)
                elif cmd == '2':
                    data = input('请输入车主名')
                    search('driverName', data)
                elif cmd == '3':
                    data = input('请输入车主身份证号码')
                    search('driverID', data)
            else:
                print('命令错误！')
        else:
            return

def addRecord():
    carPlateNum  =input('请输入车牌号: ')
    driverName = input('请输入车主名: ')
    driverId = input('请输入车主身份证号: ')
    records = input('请输入未处理违章数量: ')
    sql = "insert into info(carPlateNum, driverName,driverID, records)"
    sql2 = sql + "values ('%s' , '%s', '%s', '%s')" % (carPlateNum, driverName, driverId, records)
    cursor.execute(sql2)
    db.commit()


def showInfo():
    sql = "select * from info"
    cursor.execute(sql)
    tmp = cursor.fetchall()
    print('-----------------------------')
    if tmp:
        for x in tmp:
            print(fmt.format(' 车牌号:', x[0]))
            print(fmt.format(' 车主:', x[1]))
            print(fmt.format(' 身份证号:', x[2]))
            print(' 未处理违章:   ', x[3])
            print('-----------------------------')

    else:
        print("[未查询到记录]")


def deleteRecord(carPlateNum):
    # sql = "delete from info where driverName = ('%s')" %(name)
    # sql = "delete from info where records = '1'"
    sql = "delete from info where carPlateNum = '%s'" % (carPlateNum)
    # input = [1]
    cursor.execute(sql)
    db.commit()


menu2 = '''
        【请选择修改对象】
        1. 车牌号    
        2. 车主      
        3. 身份证号   
        4. 未处理记录
        0. 返回    
'''
menu3 = '''
        【请选择查询对象】
        1. 车牌号    
        2. 车主      
        3. 身份证号   
        0. 返回    
'''

def update(column, data ,num):
    sql = "update info set %s = %d where carPlateNum = '%s' "%(column, data, num)
    cursor.execute(sql)
    db.commit()
    print('修改成功')

def updateRecord():
    cpn = input('请输入车牌号：')
    while running:
        print(menu2)
        cmd = input()
        if cmd != '0':
            if commands(cmd) is not None:
                if cmd == '1':
                    # new = input('请输入新的车牌号')
                    # update('carPlateNum', new, cpn)
                    print('暂不支持车牌号修改')
                elif cmd == '2':
                    new = input('请输入新的数据：')
                    update('driverName', new, cpn)
                elif cmd == '3':
                    new = input('请输入新的数据：')
                    update('driverID', new, cpn)
                elif cmd == '4':
                    new = int(input('请输入新的数据'))
                    update('records', new, cpn)
            else:
                print('Unknown Command')
        else:
            return



menu = """
         主菜单
    ————————————————
    |    1. 查询    |
    |    2. 显示    |
    |    3. 删除    | 
    |    4. 新增    |
    |    5. 修改    |
    |    q. 退出    |
    ————————————————
"""
running = True

menu_dict = {
    "1": "Command 1",
    "2": "Command 2",
    "3": "Command 3",
    "4": "Command 4",
    "5": "Command 5"
}


def commands(args):
    command = menu_dict.get(args)
    return command


if __name__ == '__main__':
    while running:
        print(menu)
        cmd = input()
        if cmd != 'q':
            if commands(cmd) is not None:
                if cmd == '1':
                    # print('Command 1')
                    searchInfo()
                elif cmd == '2':
                    # print('Command 2')
                    showInfo()
                elif cmd == '3':
                    # print('Command 3')
                    deleteItem = input('请输入要删除的对象')
                    deleteRecord(deleteItem)
                elif cmd == '4':
                    addRecord()
                elif cmd == '5':
                    updateRecord()
            else:
                print('Unknown Command')
        else:
            print('正在退出...')
            sys.exit()
