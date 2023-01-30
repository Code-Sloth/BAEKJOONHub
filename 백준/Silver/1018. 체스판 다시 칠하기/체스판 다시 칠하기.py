import sys
input = sys.stdin.readline


li_b = [['B']*8 for _ in range(8)]
li_w = [['W']*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            li_b[i][j] = 'W'
            li_w[i][j] = 'B'

n, m = map(int,input().split())            
li = [list(input().strip()) for _ in range(n)]

li_tb = []
li_tw = []

for ii in range(n-7):
    for jj in range(m-7):
        t_b = 0
        t_w = 0
        for i in range(ii,ii+8):
            for j in range(jj,jj+8):
                if li[i][j] != li_b[i-ii][j-jj]:
                    t_b += 1
                elif li[i][j] != li_w[i-ii][j-jj]:
                    t_w += 1
        li_tb.append(t_b)
        li_tw.append(t_w)

print(min(min(li_tb),min(li_tw)))