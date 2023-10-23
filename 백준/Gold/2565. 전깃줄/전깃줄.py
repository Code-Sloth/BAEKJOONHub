import sys
input = sys.stdin.readline

n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [0] * n

for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))