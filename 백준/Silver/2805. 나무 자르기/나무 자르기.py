import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int,input().split())
g = list(map(int,input().split()))

def binary(st,end):
    if st > end: return end
    
    mid = (st+end)//2
    length = 0

    for i in g:
        if i > mid:
            length += i - mid

    if length >= m:
        return binary(mid+1, end)
    else:
        return binary(st, mid-1)

print(binary(1,max(g)-1))