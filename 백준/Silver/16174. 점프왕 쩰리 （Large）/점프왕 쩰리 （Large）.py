import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
vi = [[0]*n for _ in range(n)]

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        d = g[x][y]
        if d > 0:
            for dx,dy in [(0,d),(d,0)]:
                nx,ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not vi[nx][ny]:
                    if g[nx][ny] == -1:
                        print('HaruHaru')
                        sys.exit()
                    vi[nx][ny] = 1
                    q.append((nx,ny))
    return print('Hing')

bfs(0,0)