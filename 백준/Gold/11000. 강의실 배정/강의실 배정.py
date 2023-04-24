import sys
input = sys.stdin.readline

import heapq as hq

n = int(input())
g = sorted(list(map(int,input().split())) for _ in range(n))
q = []

for st, end in g:
    if q and q[0] <= st:
        hq.heappop(q)
    hq.heappush(q, end)

print(len(q))