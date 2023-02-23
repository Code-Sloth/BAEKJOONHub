import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
st, end = map(int,input().split())
m = int(input())
g = [[] for _ in range(n+1)]
vi = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    g[a] += [b]
    g[b] += [a]

def dfs(x,t):
    vi[x] = 1
    if x == end: print(t); sys.exit()
    for nx in g[x]:
        if not vi[nx]:
            dfs(nx,t+1)

if not dfs(st,0): print(-1)