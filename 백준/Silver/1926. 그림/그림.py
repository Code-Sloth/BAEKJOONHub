import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y):
    global t
    g[x][y] = 0
    for dx,dy in d:
        nx,ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
            t += 1
            g[nx][ny] = 0
            dfs(nx,ny)
    return 1

cnt = []
area = 0
if sum(map(sum,g)) == 0:print(0,0,sep='\n')
else:
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                t = 1
                area += dfs(i,j)
                cnt.append(t)

    print(area,max(cnt),sep = '\n')