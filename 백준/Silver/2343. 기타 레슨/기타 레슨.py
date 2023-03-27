import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
g = list(map(int,input().split()))
mn = int(1e9)

def binary(st,end):
    global mn

    if st > end: return
    mid = (st+end)//2
    sum_g = 0
    t = m

    for i in range(n):
        if sum_g + g[i] <= mid:
            sum_g += g[i]
        else: 
            t -= 1
            sum_g = g[i]
        if not t: break
    
    if not t:
        return binary(mid+1, end)
    else:
        mn = min(mn,mid)
        return binary(st, mid-1)

binary(max(g),sum(g))
print(mn)