import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int,input().split())
g = [list(input().rstrip()) for _ in range(n)]
vi = [[0]*m for _ in range(n)]

def dfs1(x,y):
    if y < m and g[x][y] == '-':
        vi[x][y] = 1
        dfs1(x,y+1)
    return 1

def dfs2(x,y):
    if x < n and g[x][y] == '|':
        vi[x][y] = 1
        dfs2(x+1,y)
    return 1

t = 0
for i in range(n):
    for j in range(m):
        if not vi[i][j]:
            if g[i][j] == '-':
                t += dfs1(i,j)
            else:
                t += dfs2(i,j)
print(t)