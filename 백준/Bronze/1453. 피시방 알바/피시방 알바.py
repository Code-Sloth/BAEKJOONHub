import sys
input = sys.stdin.readline

li = [0] * 101
t = 0
for _ in range(int(input())):
    nums = list(map(int,input().split()))
    for i in nums:
        if li[i]:
            t += 1
        else:li[i] += 1
print(t)