n = int(input())
g = [[' ']*(4*n-3) for _ in range(4*n-1)]

def star(n,i,j):
    if n == 1: return
    
    line_i = 4*n-1 # 세로 줄 수
    line_j = 4*n-3 # 가로 줄 수

    for k in range(line_i):
        g[i+k][j] = '*' # 세로 첫번째 줄
        if k > 1:
            g[i+k][j+line_j-1] = '*' # 세로 마지막 줄
            if k < line_i-2:
                g[i+k][j+2] = '*' # 세로 두번째 줄
    for k in range(line_j):
        g[i][j+k] = '*' # 가로 첫번째 줄
        g[i+line_i-1][j+k] = '*' # 가로 마지막 줄
        if k > 1:
            g[i+2][j+k] = '*' # 가로 두번째 줄
    star(n-1,i+2,j+2)

if n == 1:
    print('*')
else:
    star(n,0,0)
    for i in g:
        print(''.join(i).rstrip())