import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
t = 0

def dfs(x,y):
    global t
    if g[x][y] > 0:
        d = g[x][y]
        for dx,dy in [(0,d),(d,0)]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == -1:
                    t = 1
                    return
                else: dfs(nx,ny)

dfs(0,0)
print('HaruHaru') if t else print('Hing')