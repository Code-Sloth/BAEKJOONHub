import sys
input = sys.stdin.readline

r,c = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
se = set()
index = set()

for x in range(r):
    for y in range(c):
        if g[x][y] == 'X':
            index.add((x,y))
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
    if (x,y) in index:
        index.remove((x,y))

x = sorted(index, key=lambda x:x[0])
y = sorted(index, key=lambda x:x[1])

for i in range(r):
    if x[0][0] <= i <= x[-1][0]:
        print(''.join(g[i][y[0][1]:y[-1][1]+1]))