import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if not g[i][j]: print(0, end=' ')
        else: print(g[i][j]-2, end=' ')
        if j == m-1:
            print()