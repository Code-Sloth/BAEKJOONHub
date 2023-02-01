import sys
input = sys.stdin.readline
from collections import deque

n, m, r = map(int,input().split())
g = [[] for _ in range(n+1)]
vi = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]

def dfs(v):
    vi[v] = 1
    print(v,end=' ')
    g[v].sort()
    for i in g[v]:
        if not vi[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    vi = [0] * (n+1)
    vi[v] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')
        g[v].sort()
        for i in g[v]:
            if not vi[i]:
                q.append(i)
                vi[i] = 1

dfs(r)
print()
bfs(r)