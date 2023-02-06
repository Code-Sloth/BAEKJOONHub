import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
q = deque([])
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

for i in range(n):
    for j in range(m):
        if g[i][j]: q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not g[nx][ny]:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))
    return max(map(max,g))

print(bfs()-1)