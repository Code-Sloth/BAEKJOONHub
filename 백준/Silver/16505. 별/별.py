import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
g = [[' ']*(2**n) for _ in range(2**n)]

def star(n,i,j):
    if n == 0:
        g[i][j] = '*'
        return
    if n == 1:
        g[i][j],g[i][j+1],g[i+1][j] = '*','*','*'
    star(n-1,i,j)
    star(n-1,i+2**n//2,j)
    star(n-1,i,j+2**n//2)

star(n,0,0)
for i in g:
    print(''.join(i).rstrip())