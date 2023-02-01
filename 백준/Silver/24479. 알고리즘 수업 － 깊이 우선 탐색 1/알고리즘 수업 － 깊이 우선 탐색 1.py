import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v):
    global t
    vi[v] = t
    g[v].sort()
    for i in g[v]:
        if not vi[i]:
            t += 1
            dfs(i)

n, m, r = map(int,input().split())
vi = [0] * (n+1)
g = [[] for _ in range(n+1)]
t = 1

for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dfs(r)

for i in vi[1:]:
    print(i)