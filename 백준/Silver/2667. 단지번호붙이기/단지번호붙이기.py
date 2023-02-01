import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
g = [list(map(int,input().strip())) for _ in range(n)]
t = 0
result = 0
tt = []
d = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(i,j):
    global t
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if g[i][j]:
        t += 1
        g[i][j] = 0
        for dx, dy in d:
            nx, ny = i + dx, j + dy
            dfs(nx,ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            tt.append(t)
            t = 0
print(result,*sorted(tt),sep='\n')