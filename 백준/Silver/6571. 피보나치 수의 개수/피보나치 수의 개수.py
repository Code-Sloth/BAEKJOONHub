while 1:
    n, m = map(int,input().split())
    if n == 0 and m == 0: break
    t = 0
    a = 1
    b = 1
    while 1:
        a,b = b,a+b
        if a >= n: t += 1
        if a > m: break
    print(t-1)