import sys
input = sys.stdin.readline

r,c,n = map(int,input().split())
g = [list(input().rstrip()) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
n -= 1

def func1():
    for i in range(r):
        for j in range(c):
            if g[i][j] == 'O':
                se.add((i,j))

def func2():
    g = [['O']*c for _ in range(r)]
    return g

def func3():
    for x,y in se:
        g[x][y] = '.'
        for dx,dy in d:
            if 0 <= x+dx < r and 0 <= y+dy < c:
                g[x+dx][y+dy] = '.'

while 1:
    se = set()
    
    func1()
    if not n: break

    g = func2()
    n -= 1
    if not n: break

    func3()
    n -= 1
    if not n: break

for i in g:
    print(''.join(i))