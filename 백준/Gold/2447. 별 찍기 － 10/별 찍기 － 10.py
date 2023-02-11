import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
origi_n = n
cnt = n // 3
g = [['*']*n for _ in range(n)]

def star(n):
    if n < 3: return
    for iii in range(0,origi_n,n):
        for jjj in range(0,origi_n,n):
            i,j = iii,jjj
            for ii in range(n//3,n-n//3):
                for jj in range(n//3,n-n//3):
                    if g[i+ii][j+jj] == '*':
                        g[i+ii][j+jj] = ' '
    star(n//3)

star(n)
for i in g:
    print(''.join(i),end='\n')