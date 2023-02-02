import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

from collections import deque

n, m = map(int,input().split())
g = [list(map(int,input().strip())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
t = 1
no = 0
def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))
    return g[n-1][m-1]

print(bfs(0,0))