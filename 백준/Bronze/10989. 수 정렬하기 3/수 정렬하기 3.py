import sys
input = sys.stdin.readline


li = [0] * 10001

for i in range(int(input())):
    li[int(input())] += 1

for j in range(10001):
    if li[j] != 0:
        for _ in range(li[j]):
            print(j)