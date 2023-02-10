import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
d = [0] * (n+1)
di = {0:0,1:1}
def f(x):
    if x in di: return di[x]
    if d[x] != 0: return d[x]
    d[x] = f(x-1) + f(x-2)
    return d[x]
print(f(n))