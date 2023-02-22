import sys
input = sys.stdin.readline
import heapq as hq

INF = int(1e9)
n, m, k, x = map(int,input().split())
g = [[] for _ in range(n+1)]
dis = [INF] * (n+1)

for _ in range(m):
  a, b = map(int,input().split())
  g[a].append(b)

def dijkstra(x):
  q = []
  hq.heappush(q, (0, x))
  dis[x] = 0
  while q:
    d, now = hq.heappop(q)
    if dis[now] < d:continue
    if d == k:
      cnt.append(now)
      continue
    for i in g[now]:
      cost = d + 1
      if cost < dis[i]:
        dis[i] = cost
        hq.heappush(q,(cost, i))
cnt = []
dijkstra(x)
print(*cnt,sep='\n') if cnt else print(-1)