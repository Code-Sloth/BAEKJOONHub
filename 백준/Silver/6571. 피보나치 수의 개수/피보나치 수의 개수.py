d = [1,2]
n = 2
while d[-1] <= 10**100:
    d.append(d[n-1] + d[n-2])
    n += 1

while 1:
    n, m = map(int,input().split())
    if n == 0 and m == 0: break
    t = 0
    for i in d:
        if n <= i <= m:
            t += 1
    print(t)