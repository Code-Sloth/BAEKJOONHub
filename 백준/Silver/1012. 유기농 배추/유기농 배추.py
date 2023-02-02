import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

d = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if g[x][y]:
        g[x][y] = 0
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            dfs(nx,ny)
        return True
    return False

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    g = [[0]*m for __ in range(n)]
    for __ in range(k):
        x,y = map(int,input().split())
        g[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                result += dfs(i,j)
    print(result)