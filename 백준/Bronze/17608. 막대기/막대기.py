import sys
input = sys.stdin.readline

li = [int(input()) for _ in range(int(input()))]
max_q = li[-1]

t = 1
for i in reversed(li):
    if i > max_q:
        max_q = i
        t += 1
print(t)