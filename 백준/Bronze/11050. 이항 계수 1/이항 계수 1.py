import sys

input = sys.stdin.readline

n, k = map(int,input().split())
up = 1
down = 1
for i in range(n,n-k,-1):
    up *= i
for j in range(k,1,-1):
    down *= j
print(up//down)