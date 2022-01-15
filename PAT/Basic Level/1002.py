instr = input().split()
length = int(instr[0])
a1, a2, a3, a4, a5 = 'N', 'N', 'N', 'N', 'N'
a1found = 0
a2found = 0
a3found = 0
a4found = 0
a5found = 0
flag = 1
a4num = 0
for i in range(length):
    x = int(instr[i + 1])
    if x % 5 == 0 and x % 2 == 0:
        if a1found == 0:
            a1 = 0
            a1found = 1
        a1 += x
    elif x % 5 == 1:
        if a2found == 0:
            a2 = 0
            a2found = 1
        a2 += flag * x
        flag *= -1
    elif x % 5 == 2:
        if a3found == 0:
            a3 = 0
            a3found = 1
        a3 += 1
    elif x % 5 == 3:
        if a4found == 0:
            a4 = 0
            a4found = 1
        a4 += x
        a4num += 1
    elif x % 5 == 4:
        if a5found == 0:
            a5 = 0
            a5found = 1
        if x > a5:
            a5 = x
if type(a4) != str:
    a4 = round(a4 / a4num, 1)
print(str(a1) + " " + str(a2) + " " + str(a3) + ' ' + str(a4) + ' ' + str(a5))
