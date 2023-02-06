import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

from collections import deque

def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        if x == end1 and y == end2:
            return g[x][y]
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not g[nx][ny]:
                g[nx][ny] = g[x][y] + 1
                q.append((nx,ny))


for _ in range(int(input())):
    n = int(input())
    st1,st2 = map(int,input().split())
    end1,end2 = map(int,input().split())
    g = [[0] * n for _ in range(n)]
    d = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    print(bfs(st1,st2))