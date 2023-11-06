import sys
input = sys.stdin.readline

from collections import deque

n, m=map(int, input().split())
g = [0]*100001
q = deque([n])
g[n] = 1

while q:
    x = q.popleft()

    if x == m:
        print(g[m] - 1)
        break

    for nx in (2*x, x-1, x+1):
        if 0 <= nx <= 100000 and not g[nx]:
            if nx == 2*x:
                g[nx] = g[x]
                q.append(nx)
            else:
                g[nx] = g[x] + 1
                q.append(nx)