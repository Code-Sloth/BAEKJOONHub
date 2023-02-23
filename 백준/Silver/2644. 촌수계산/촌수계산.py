import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
st, end = map(int,input().split())
m = int(input())
g = [[] for _ in range(n+1)]
dis = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]

def bfs(x):
    q = deque([x])
    dis[x] = 1
    while q:
        x = q.popleft()
        if x == end: print(dis[x]-1); return 1
        for nx in g[x]:
            if not dis[nx]:
                dis[nx] = dis[x] + 1
                q.append(nx)
    return 0

if not bfs(st):print(-1)