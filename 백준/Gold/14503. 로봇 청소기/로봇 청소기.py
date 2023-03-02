import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int,input().split())
r,c,d = map(int,input().split())
g = [list(map(int,input().split())) for _ in range(n)]
direc = [(-1,0),(0,1),(1,0),(0,-1)]
se = set()
for i in range(n):
    for j in range(m):
        if g[i][j]:
            se.add((i,j))

def dfs(x,y,d,t):
    if not g[x][y]:
        g[x][y] = 1
        t += 1
    for _ in range(4):
        d = (d+3) % 4
        if not g[x+direc[d][0]][y+direc[d][1]]:
            dfs(x+direc[d][0],y+direc[d][1],d,t)
    else:
        if (x+direc[(d+2)%4][0],y+direc[(d+2)%4][1]) in se:
            print(t)
            sys.exit()
        else:
            dfs(x+direc[(d+2)%4][0],y+direc[(d+2)%4][1],d,t)

dfs(r,c,d,0)