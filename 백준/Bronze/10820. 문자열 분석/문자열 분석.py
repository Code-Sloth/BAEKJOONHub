import sys
input = sys.stdin.readline

while 1:
    s = input()
    if not s: break
    a=b=c=d=0
    for i in s:
        if i.islower(): a += 1
        elif i.isupper(): b += 1
        elif i.isnumeric(): c += 1
        elif i == ' ': d += 1
    print(a,b,c,d)
