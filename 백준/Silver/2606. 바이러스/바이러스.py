import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import deque

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
vi = [0] * (n+1)

def bfs(v):
    q = deque([v])
    vi[v] = 1
    while q:
        v = q.popleft()
        g[v].sort()
        for i in g[v]:
            if not vi[i]:
                q.append(i)
                vi[i] = 1
bfs(1)
print(vi.count(1)-1)