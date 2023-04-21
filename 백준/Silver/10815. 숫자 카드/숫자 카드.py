import sys
input = sys.stdin.readline

n = int(input())
se = set(list(map(int,input().split())))
m = int(input())
g = list(map(int,input().split()))

result = [0] * m

for i in range(m):
    if g[i] in se:
        result[i] ^= 1

print(' '.join(map(str,result)))