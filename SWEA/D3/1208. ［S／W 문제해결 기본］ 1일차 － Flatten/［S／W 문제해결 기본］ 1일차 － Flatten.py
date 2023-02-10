for t in range(1,11):
    n = int(input())
    g = sorted(list(map(int,input().split())))
    while n > 0:
        g[0] += 1
        g[-1] -= 1
        g.sort()
        n -= 1
    print(f'#{t} {g[-1] - g[0]}')