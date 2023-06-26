from collections import deque
d = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y,n,m,g,le,end):
    q = deque([(x,y)])
    vi = [[0] * m for _ in range(n)]
    vi[x][y] = 1
    while q:
      x,y = q.popleft()
      for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] in ('S','O','L','E'):
          if not vi[nx][ny]:
            vi[nx][ny] = vi[x][y] + 1
            q.append((nx,ny))

    return vi[le[0]][le[1]], vi[end[0]][end[1]]
          
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    for i in range(len(maps)):
      for j in range(len(maps[0])):
        if maps[i][j] == 'S':
          st = (i,j)
        elif maps[i][j] == 'L':
          le = (i,j)
        elif maps[i][j] == 'E':
          end = (i,j)
    
    ans_le, ans_end = bfs(st[0],st[1],n,m,maps,le,end)
    answer += ans_le - 1
    ans_le2, ans_end2 = bfs(le[0],le[1],n,m,maps,le,end)
    answer += ans_end2 - 1

    if ans_le and ans_end2:
      return answer
    else:
      return -1