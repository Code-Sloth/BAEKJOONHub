import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int,input().split())
g = [int(input()) for i in range(n)]

def binary(st,end):
    mid = (st+end)//2
    if st > end: return mid
    length = 0

    for i in g:
        length += i//mid

    if length >= k:
        return binary(mid+1, end)
    else:
        return binary(st, mid-1)

print(binary(1,max(g)))