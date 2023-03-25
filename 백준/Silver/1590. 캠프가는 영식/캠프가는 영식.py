import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, time = map(int,input().split())

def binary(st,end):
    if st > end: return -1
    mid = (st+end)//2

    if g[mid] == time: return 0
    elif g[mid] < time:
        if g[mid] < time <= g[mid+1]:
            return g[mid+1] - time
        else:
            return binary(mid+1,end)
    else:
        if g[mid-1] < time < g[mid]:
            return g[mid] - time
        else:
            return binary(st, mid-1)

li = []
mn = int(1e9)
for _ in range(n):
    start, dis, cnt = map(int,input().split())
    g = [start + dis*i for i in range(cnt+1)]
    if time > start + dis*(cnt-1): li.append(-1)
    elif time < start: li.append(start-time)
    else:
        li.append(binary(0,cnt-1))
for i in li:
    if i >= 0:
        mn = min(mn,i)
if mn == int(1e9):
    print(-1)
else:
    print(mn)