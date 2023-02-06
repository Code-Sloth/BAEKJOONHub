import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]
vi = [0] * (n+1)

def dfs(x):
    vi[x] = 1
    for i in g[x]:
        if not vi[i]:
            vi[i] = 1
            dfs(i)
    return vi.count(1)-1

print(dfs(1))