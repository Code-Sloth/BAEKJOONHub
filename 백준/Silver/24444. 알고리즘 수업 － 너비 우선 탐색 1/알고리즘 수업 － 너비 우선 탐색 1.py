import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import deque
def bfs(v):
    global t
    q = deque([v])
    vi[v] = t
    while q:
        v = q.popleft()
        g[v].sort()
        for i in g[v]:
            if not vi[i]:
                q.append(i)
                t += 1
                vi[i] = t

n, m, r = map(int,input().split())
vi = [0] * (n+1)
g = [[] for _ in range(n+1)]
t = 1

for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
    
bfs(r)
for i in vi[1:]:
    print(i)