n = int(input())
g = [[' ']*(4*n-3) for _ in range(4*n-3)]

def star(n,i,j):
    if n == 1: 
        g[i][j] = '*'
        return
    line = 4*n-3
    for k in range(line):
        g[i+k][j] = '*'
        g[i+line-1][j+k] = '*'
        g[i][j+k] = '*'
        g[i+k][j+line-1] = '*'
    star(n-1,i+2,j+2)

star(n,0,0)
for i in g:
    print(''.join(i).rstrip())