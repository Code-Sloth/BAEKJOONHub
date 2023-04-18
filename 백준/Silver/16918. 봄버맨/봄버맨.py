import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
n -= 1

while 1:
    se = set()
    for i in range(r):
        for j in range(c):
            if g[i][j] == 'O':
                se.add((i,j))

    if not n: break

    g = [['O']*c for _ in range(r)]

    n -= 1
    if not n: break

    for x,y in se:
        g[x][y] = '.'
        for dx,dy in d:
            if 0 <= x+dx < r and 0 <= y+dy < c:
                g[x+dx][y+dy] = '.'
    n -= 1
    if not n: break

for i in g:
    print(''.join(i))