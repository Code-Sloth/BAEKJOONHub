import string

s = list(input())
t = 0
abc = string.ascii_uppercase

for i in s:
    if i in abc[0:3]: # 2
        t += 3
    elif i in abc[3:6]: # 3
        t += 4
    elif i in abc[6:9]: # 4
        t += 5
    elif i in abc[9:12]: # 5
        t += 6
    elif i in abc[12:15]: # 6
        t += 7    
    elif i in abc[15:19]: # 7
        t += 8
    elif i in abc[19:22]: # 8
        t += 9
    elif i in abc[22:26]: # 9
        t += 10

print(t)