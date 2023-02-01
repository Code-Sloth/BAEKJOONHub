import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

from collections import deque

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]
vi = [0] * (n+1)

def dfs(v):
    vi[v] = 1
    for i in g[v]:
        if not vi[i]:
            dfs(i)

dfs(1)
print(vi.count(1)-1)