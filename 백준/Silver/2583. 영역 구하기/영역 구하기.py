import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int,input().split())
g  = [[0]*m for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y,t):
    q = deque([(x,y)])
    g[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not g[nx][ny]:
                t += 1
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))
    return t

for _ in range(k):
    j1, i1, j2, i2 = map(int,input().split())
    for i in range(i1,i2):
        for j in range(j1,j2):
            if not g[i][j]: g[i][j] = 1

cnt = []
for i in range(n):
    for j in range(m):
        if not g[i][j]:
            cnt.append(bfs(i,j,1))
print(len(cnt))
print(*sorted(cnt))