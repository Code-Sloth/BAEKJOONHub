import sys

input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))
near = m
m1 = 0

for i in range(n-2):
    m1 += 1
    m2 = m1
    for j in range(m1,n-1):
        m2 += 1
        for k in range(m2,n):
            if nums[i]+nums[j]+nums[k] <= m:
                sol = m - (nums[i]+nums[j]+nums[k])
                if 0 <= sol < near:
                    near = m - (nums[i]+nums[j]+nums[k])
                    sum_nums = nums[i]+nums[j]+nums[k]
print(sum_nums)