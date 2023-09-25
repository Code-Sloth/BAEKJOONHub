from collections import deque

n, m = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
d = [(1,0), (0,1), (-1,0), (0,-1)]

for i in range(n):
    for j in range(m):
        if g[i][j] == 'I':
            sx, sy = i, j

def bfs(x, y):
    vi = [[0] * m for _ in range(n)]
    q = deque([(x, y)])
    vi[x][y] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        for dx,dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != 'X' and not vi[nx][ny]:
                vi[nx][ny] = 1
                q.append((nx, ny))
                if g[nx][ny] == 'P':
                    cnt += 1

    return cnt

sol = bfs(sx, sy)
print('TT') if sol == 0 else print(sol)