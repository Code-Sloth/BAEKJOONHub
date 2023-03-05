import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a,b = map(int,input().split())

def dfs(a,t):
    if a > b:return
    if a == b: print(t); sys.exit()
    dfs(a*2,t+1)
    dfs(a*10+1,t+1)

dfs(a,1)
print(-1)