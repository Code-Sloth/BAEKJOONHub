import sys
input = sys.stdin.readline

from collections import deque

q = deque([[0]*100 for __ in range(100)])

for _ in range(int(input())):
    x, y = map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            if not q[j][i]:
                q[j][i] += 1
t = 0
for k in q:
    t += k.count(1)
print(t)