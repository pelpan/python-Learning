n = int(input())
for i in range(n):
    string = input().split()
    x = int(string[0])
    y = int(string[1])
    z = int(string[2])
    if x+y > z:
        print("Case #"+str(i+1)+": true")
    else:
        print("Case #"+str(i+1)+": false")
