import sys
input = sys.stdin.readline

n = int(input())
ord = list(input().rstrip())
li = [['#'] * 101 for _ in range(101)]
li_i = [50]
li_j = [50]
i,j = 50,50
li[50][50] = '.'
t = 4

for order in ord:
    if order == 'R':
        t += 1
    elif order == 'L':
        t -= 1
    elif order == 'F':
        if t % 4 == 0: 
            i += 1
            li[i][j] = '.'
            li_i.append(i)
        elif t % 4 == 1: 
            j -= 1
            li[i][j] = '.'
            li_j.append(j)
        elif t % 4 == 2: 
            i -= 1
            li[i][j] = '.'
            li_i.append(i)
        else: 
            j += 1
            li[i][j] = '.'
            li_j.append(j)

for ii in range(min(li_i),max(li_i)+1):
    for jj in range(min(li_j),max(li_j)+1):
        print(li[ii][jj],end='')
    print()