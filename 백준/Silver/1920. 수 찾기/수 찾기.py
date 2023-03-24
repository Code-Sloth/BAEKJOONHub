import sys
input = sys.stdin.readline

n = int(input())
g = sorted(map(int,input().split()))
m = int(input())
mg = map(int, input().split())

def binary(a,st,ed):
    if st > ed: return
    mid = (st+ed)//2

    if g[mid] == a:
        return 1
    elif g[mid] < a:
        return binary(a,mid+1,ed)
    else:
        return binary(a,st,mid-1)

for i in mg:
    print(1) if binary(i,0,n-1) else print(0)