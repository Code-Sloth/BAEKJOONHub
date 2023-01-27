import sys
input = sys.stdin.readline

import heapq as hq
h = []

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not h:print(0)
        else:
            a = hq.heappop(h)
            print(a[1])
    else:
        hq.heappush(h,(-n,n)) if n < 0 else hq.heappush(h,(n,n))