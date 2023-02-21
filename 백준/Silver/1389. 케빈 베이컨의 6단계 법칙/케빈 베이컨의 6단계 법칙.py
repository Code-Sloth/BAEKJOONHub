import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]

def bfs(x,end):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == end:
            cnt.append(vi[x])
        for nx in g[x]:
            if not vi[nx]:
                vi[nx] = vi[x] + 1
                q.append(nx)

kevin = []
for i in range(1,n+1):
    cnt = []
    for j in range(1+n+1):
        if i != j:
            vi = [0] * (n+1)
            bfs(i,j)
    kevin.append(sum(cnt))
print(kevin.index(min(kevin))+1)