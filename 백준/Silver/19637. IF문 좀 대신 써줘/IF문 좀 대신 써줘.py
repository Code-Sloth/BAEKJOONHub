import sys
input = sys.stdin.readline

import bisect

n, m = map(int, input().split())
name, nums = [], []

for i in range(n):
    a,b = input().split()
    name.append(a)
    nums.append(int(b))

for _ in range(m):
    i = bisect.bisect_left(nums, int(input()))
    print(name[i])