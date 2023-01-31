import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
nums = list(map(int,input().split()))
nums_c = Counter(nums)
n = int(input())
li = list(map(int,input().split()))
for i in li:
    print(nums_c[i],end=' ')