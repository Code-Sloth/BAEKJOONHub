import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int,input().split())

def binary(st, end):
    if st > end: return 'NO'
    mid = (st+end)//2
    sum_mid = (mid+1)*(n-mid+1)

    if sum_mid == k: return 'YES'
    elif sum_mid < k:
        return binary(mid+1, end)
    else:
        return binary(st, mid-1)

print(binary(0,n//2))