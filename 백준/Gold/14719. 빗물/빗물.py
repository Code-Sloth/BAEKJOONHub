import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = list(map(int,input().split()))

t = 0
for y in range(1,n+1):
    temp = False
    flag = 0
    for x in range(m):
        if g[x] >= y:
            if temp:
                t += x - flag - 1
            flag = x
            temp = True

print(t)