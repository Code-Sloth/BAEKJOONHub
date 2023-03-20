import sys
input = sys.stdin.readline

n, m = map(int,input().split())
snow = [0] + list(map(int,input().split()))
maxsize = -1

def dfs(x, t, size):
    global maxsize
    if t < 0: return

    maxsize = max(maxsize,size)
    
    if x+1 <= n:
        dfs(x+1, t-1, size+snow[x+1])
    if x+2 <= n:
        dfs(x+2, t-1, size//2+snow[x+2])

dfs(0,m,1)
print(maxsize)