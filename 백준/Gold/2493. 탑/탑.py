import sys
input = sys.stdin.readline

n = int(input())
g = [0] + list(map(int,input().split()))
result = [0] * (n+1)

for right in range(1, n+1):
    left = right-1
    while left:
        if g[left] >= g[right]:
            result[right] = left
            break
        else:
            left = result[left]

print(' '.join(map(str,result[1:])))