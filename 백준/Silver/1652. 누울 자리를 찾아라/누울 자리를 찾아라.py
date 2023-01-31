import sys
input = sys.stdin.readline

n = int(input())
li = [list(input().strip()) for _ in range(n)]
li2 = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        li2[i][j] = li[j][i]

for i in range(n):
    li[i] = ''.join(li[i])
    li2[i] = ''.join(li2[i])

x,y = 0,0
for i in range(n):
    for j in li[i].split('X'):
        if '..' in j: x += 1
    for j in li2[i].split('X'):
        if '..' in j: y += 1
print(x,y)