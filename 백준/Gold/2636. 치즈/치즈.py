import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y):
    q = deque([(x,y)])
    vi = [[0] * m for _ in range(n)]
    t = 0
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny] and not vi[nx][ny]:
                    vi[nx][ny] = 1
                    q.append((nx,ny))

                elif graph[nx][ny]:
                    graph[nx][ny] = 0
                    vi[nx][ny] = 1
                    t += 1
    return t

result = []
time = 0
while 1:
    t = bfs(0,0)
    result.append(t)
    if t == 0:break
    time += 1

print(time)
print(result[-2])