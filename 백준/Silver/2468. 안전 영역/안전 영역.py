import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
cnt = []

def bfs(x,y,height):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not vi[nx][ny] and g[nx][ny] > height:
                vi[nx][ny] = 1
                q.append((nx,ny))
    return 1

 
for h in range(min(map(min,g))-1,max(map(max,g))):
    t = 0
    vi = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] > h and not vi[i][j]:
                t += bfs(i,j,h)
    cnt.append(t)
print(max(cnt))