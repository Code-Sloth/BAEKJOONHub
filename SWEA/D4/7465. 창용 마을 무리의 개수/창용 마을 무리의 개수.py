def dfs(x):
    vi[x] = 1
    for i in g[x]:
        if not vi[i]:
            vi[i] = 1
            dfs(i)
    return 1

for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    g = [[] for _ in range(n+1)]
    vi = [0] * (n+1)
    for i in range(m):
        a, b = map(int,input().split())
        g[a] += [b]
        g[b] += [a]
    cnt = 0
    for i in range(1,n+1):
        if not vi[i]:
            cnt += dfs(i)
    print(f'#{t} {cnt}')