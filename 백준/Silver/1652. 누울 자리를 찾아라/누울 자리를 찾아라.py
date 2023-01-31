import sys
input = sys.stdin.readline

n = int(input())
li = [list(input().strip()) for _ in range(n)]
xx,yy = 0,0

for i in range(n):
    x = 0
    for j in range(n):
        if li[i][j] == '.': x += 1
        else: x = 0
        if x == 2:
            xx += 1

for i in range(n):
    y = 0
    for j in range(n):
        if li[j][i] == '.': y += 1
        else: y = 0
        if y == 2:
            yy += 1

print(xx,yy)