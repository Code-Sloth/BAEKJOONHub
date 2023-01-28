import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())
    d = a
    a = a%10
    if a == 1 or a == 5 or a == 6:print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        c = b%4
        if c == 0:c=4
        print((a**c)%10)
    elif a == 9 or a == 4:
        c = b%2
        if c == 0:c=2
        print((a**c)%10)
    elif a == 0:print(10)