import sys
input = sys.stdin.readline

r,c = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
se = set()

for x in range(r):
    for y in range(c):
        if g[x][y] == 'X':
            t = 0
            for dx,dy in d:
                if 0 <= x+dx < r and 0 <= y+dy < c:
                    if g[x+dx][y+dy] == '.':
                        t += 1
                else: t += 1
            if t >= 3:
                se.add((x,y))
for x,y in se:
    g[x][y] = '.'

mxx,mxy,mnx,mny = -1,-1,int(1e9),int(1e9)
for x in range(r):
    for y in range(c):
        if g[x][y] == 'X':
            if mxx < x: mxx = x
            if mxy < y: mxy = y
            if mnx > x: mnx = x
            if mny > y: mny = y

for i in range(r):
    if mnx <= i <= mxx:
        print(''.join(g[i][mny:mxy+1]))