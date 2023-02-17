import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))

m, n = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
q = deque()
d = [(1,0),(-1,0),(0,1),(0,-1)]
t = 0
           
bfs()

max_g = -2
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1)
            sys.exit()
        elif g[i][j] > max_g:
            max_g = g[i][j]
print(max_g-1)