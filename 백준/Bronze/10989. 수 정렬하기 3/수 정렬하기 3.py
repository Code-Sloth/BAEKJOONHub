import sys

input = sys.stdin.readline

n = int(input())
li = [0] * 10001

for i in range(n):
    num = int(input())
    li[num] += 1

for j in range(10001):
    if li[j] != 0:
        for _ in range(li[j]):
            print(j)