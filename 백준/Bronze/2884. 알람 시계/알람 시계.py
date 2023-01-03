a,b=map(int,input().split())

if b>=45:
    b -= 45
    print(a,b)
elif a==0 and b<45:
    a=23
    b += 15
    print(a,b)
else:
    a -= 1
    b += 15
    print(a,b)