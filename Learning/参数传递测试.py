# -- coding: utf-8 --
# 函数参数传递测试
""" a = 10

def change(a):
    print(id(a))
    a = 20 
    print(id(a))

print(a)
print(id(a))
change(a)
print(id(a))   """ # 函数中改变a指向的对象，全局变量并未改变

""" list1 = [1,2,3,4,5]
def changelist(a):
    print(a)
    a[2] = 666

print(list1)
changelist(list1)
print(list1)  # 可变参数 """

# 函数默认参数
def defaultAgrument(a , b =35):
    print("姓名：", a)
    print("年龄：", b)
# defaultAgrument(a="潘求祺", b=20)
# defaultAgrument("张溜溜")
print("中文，你好", 10)   # 在python3中可以正常显示，在python2中会出错
print("你好%d"%10)