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
    num = int(input())
    i = bisect.bisect_left(nums, num)
    print(name[i])