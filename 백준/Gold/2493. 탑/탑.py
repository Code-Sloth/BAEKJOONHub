import sys
input = sys.stdin.readline

n = int(input())
g = list(map(int,input().split()))
result = [0] * n

for i in range(1, n):
    target = i-1
    while target > -1:
        if g[target] >= g[i]:
            result[i] = target + 1
            break
        else:
            target = result[target] - 1

print(' '.join(map(str,result)))