import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if g[i][j][k] == 1:
                    q.append((i,j,k))
    if not q: print(-1); sys.exit()
    while q:
        z, x, y = q.popleft()
        for dz,dx,dy in d:
            nz,nx,ny = z+dz,x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and 0<= nz < h and g[nz][nx][ny] == 0:
                g[nz][nx][ny] = g[z][x][y] + 1
                q.append((nz,nx,ny))

m, n, h = map(int,input().split())
g = [[list(map(int,input().split())) for _ in range(n)] for __ in range(h)]
q = deque()
d = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

bfs()

max_g = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 0: print(-1); sys.exit()
            elif g[i][j][k] > max_g: max_g = g[i][j][k]

print(max_g-1)