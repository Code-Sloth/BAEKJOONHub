import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int,input().split())
a = int(input())
q = deque([i for i in range(1,m+1)])
t = 0

for _ in range(a):
    i = int(input())
    while 1:
        if i not in q:
            if i > max(q):
                q.append(max(q)+1)
                q.popleft()
                t += 1
            if i < min(q):
                q.appendleft(min(q)-1)
                q.pop()
                t += 1
        else: break
print(t)