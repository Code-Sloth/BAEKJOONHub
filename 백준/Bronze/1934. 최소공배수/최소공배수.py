t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    n = 1
    a2 = a
    b2 = b
    while 1:
        c = a2 % b2
        n = b2
        if c == 0:
            break
        a2 = b2
        b2 = c
    if n == 1:
        print(a*b)
    else:
        print(n*((a//n)*(b//n)))