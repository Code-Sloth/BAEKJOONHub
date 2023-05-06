import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ls = len(s)
lt = len(t)

def dfs(t,lt):
    if t==s: print(1); sys.exit()
    if lt < ls: return

    if t[-1]=='A':
        dfs(t[:-1],lt-1)
    if t[-1]=='B':
        dfs(t[:-1][::-1],lt-1)

dfs(t,lt)
print(0)