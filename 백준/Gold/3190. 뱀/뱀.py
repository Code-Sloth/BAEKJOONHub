import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

from collections import deque

n = int(input())
apple = int(input())
g = [[0]*n for _ in range(n)]
for i in range(apple):
    a,b = map(int,input().split())
    g[a-1][b-1] = 2

turn = int(input())
turn_i = deque([input().split() for _ in range(turn)]+[(0,0)])
d = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌
q = deque([(0,0)])
g[0][0] = 1

def func_turn(d,dir):
    return (d+1) % 4 if dir == 'D' else (d-1) % 4

def dfs(x,y,d_index,t):
    if x < 0 or x >= n or y < 0 or y >= n or g[x][y] == 1:
        return t

    q.append((x,y))

    if g[x][y] != 2:
        a,b = q.popleft()
        g[a][b] = 0
    g[x][y] = 1

    if t == int(turn_i[0][0]):

        d_index = func_turn(d_index, turn_i[0][1])
        turn_i.popleft()
    return dfs(x+d[d_index][0], y+d[d_index][1], d_index, t+1)

print(dfs(0,1,1,1))