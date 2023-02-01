import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int,input().strip())) for _ in range(n)]
t = 0
result = 0
tt = []

def dfs(i,j):
    global t
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if g[i][j] == 1:
        t += 1
        g[i][j] = 0
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            tt.append(t)
            t = 0
print(result,*sorted(tt),sep='\n')