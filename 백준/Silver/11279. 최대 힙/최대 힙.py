import sys
input = sys.stdin.readline
import heapq as hq

h = []

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        hq.heappush(h,-n)
    else:
        print(-hq.heappop(h)) if h else print(0)