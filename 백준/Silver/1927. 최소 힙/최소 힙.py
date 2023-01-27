import sys
input = sys.stdin.readline

import heapq as hq

h = []
hq.heapify(h)

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not h:print(0)
        else:
            print(hq.heappop(h))
    else:
        hq.heappush(h,n)