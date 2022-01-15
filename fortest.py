# get = input()
# sp = get.split(" ")
# day = int(sp[1])
# first = int(sp[0])
# for i in range(day-1):
#     first += 2
#     if first >= 20:
#         break
# print(first)
"""
day = int(input())
tem = input()
daytem = tem.split(" ")
Max = 0
mm = 0
for i in range(day - 1):
    if daytem[i] < daytem[i + 1]:
        mm = mm + 1
        if mm > Max:
            Max = mm
    else:
        mm = 0
if Max != 0:
    Max = Max + 1
print(Max)
"""

str = input()
tmp = str.split(" ")
x = int(tmp[0])
y = int(tmp[1])
print(x+y)
