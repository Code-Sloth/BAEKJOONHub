import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

d = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y):
    for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny]:
            g[nx][ny] = 0
            dfs(nx,ny)
    return 1

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    g = [[0]*m for __ in range(n)]
    for ___ in range(k):
        a, b = map(int,input().split())
        g[a][b] = 1
    t = 0
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                g[i][j] = 0
                t += dfs(i,j)
    print(t)