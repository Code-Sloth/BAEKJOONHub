import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def recur(n):
    global t
    if n == 0:
        t += 1
        return
    if n < 0:
        return
    recur(n-1)
    recur(n-2)
    recur(n-3)


for _ in range(int(input())):
    t = 0
    recur(int(input()))
    print(t)