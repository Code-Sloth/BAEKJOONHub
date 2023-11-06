import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
vi = [False for _ in range(n+1)]
sol = 0

for i in range(m):
    a,b,c = map(int,input().split())
    g[a].append((c,b))
    g[b].append((c,a))

q = []
heapq.heappush(q, (0,1))

def func():
    global sol
    while q:
        x, now = heapq.heappop(q)
        if vi[now] == False:
            vi[now] = True
            sol += x
            for nx, ny in g[now]:
                heapq.heappush(q, (nx, ny))
    return sol

print(func())