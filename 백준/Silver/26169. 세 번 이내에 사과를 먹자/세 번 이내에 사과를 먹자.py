import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

g = [list(map(int,input().split())) for _ in range(5)]
r, c = map(int,input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y,t,apple):
    if apple == 2: print(1); sys.exit()
    if not t: return

    g[x][y] = -1
    for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5 and g[nx][ny] != -1:
            if g[nx][ny]:
                dfs(nx,ny,t-1,apple+1)
            else:
                dfs(nx,ny,t-1,apple)
    return 0

print(dfs(r,c,3,0))