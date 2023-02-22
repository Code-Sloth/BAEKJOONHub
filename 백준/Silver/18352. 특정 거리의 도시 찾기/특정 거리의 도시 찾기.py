import sys
input = sys.stdin.readline
from collections import deque

inf = int(1e9)
n, m, d, x = map(int,input().split())
g = [[] for _ in range(n+1)]
dis = [0]*(n+1)
cnt = []

for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]

def bfs(x):
    q = deque([x])
    dis[x] = 1
    while q:
        x = q.popleft()
        for nx in g[x]:
            if not dis[nx]:
                dis[nx] = dis[x] + 1
                q.append(nx)
        if dis[x]-1 == d:
            cnt.append(x)
            
bfs(x)
print(*sorted(cnt),sep='\n') if cnt else print(-1)