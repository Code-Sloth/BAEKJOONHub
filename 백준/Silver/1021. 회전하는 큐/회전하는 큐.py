import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int,input().split())
q = deque(range(1,n+1))
li = list(map(int,input().split()))
li_pop = []
i = 0
t = 0

while li != li_pop:
    if q[0] == li[i]:
        li_pop.append(q.popleft())
        i += 1
    else:
        if q.index(li[i]) <= len(q)//2:
            q.rotate(-1)
            t += 1
        else:
            q.rotate(1)
            t += 1
print(t)