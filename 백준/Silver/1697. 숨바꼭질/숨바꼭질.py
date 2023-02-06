import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

from collections import deque

INF = int(1e5)
st, end = map(int,input().split())
g = [0] * (INF+1)

def bfs():
    q = deque([st])
    while q:
        x = q.popleft()
        if x == end:
            print(g[x])
            break
        for nx in (x+1, x-1, x*2):
            if 0 <= nx <= INF and not g[nx]:
                g[nx] = g[x] + 1
                q.append(nx)

bfs()