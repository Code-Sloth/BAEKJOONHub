import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = []
nums2 = []
for _ in range(n):
    nums.append(list(map(int,input().split())))
for __ in range(n):
    nums2.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        print(nums[i][j] + nums2[i][j],end=' ')
    print()