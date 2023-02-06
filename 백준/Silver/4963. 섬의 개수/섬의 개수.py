import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x,y):
    g[x][y] = 0
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:continue
        if g[nx][ny]:
            dfs(nx,ny)
    return True


while 1:
    m, n = map(int,input().split())
    if m == 0 and n == 0: break
    g = [list(map(int,input().split())) for _ in range(n)]
    d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    t = 0

    for i in range(n):
        for j in range(m):
            if g[i][j]:
                t += dfs(i,j)
    print(t)