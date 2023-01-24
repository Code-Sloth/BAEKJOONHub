import sys
input = sys.stdin.readline

import math

n = int(input())
nums = list(map(int,input().split()))
b, c = map(int,input().split())
li = [0] * n
total = 0

for i in range(n):
    li[i] = nums[i] - b
    total += 1

for j in li:
    if j > 0:
        total += math.ceil(j/c)
        
print(total)