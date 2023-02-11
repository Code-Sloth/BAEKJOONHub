import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def recur(s,l,r):
    global t
    t += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    return recur(s,l+1,r-1)

def is_pal(s):
    return recur(s,0,len(s)-1)
    
for _ in range(int(input())):
    s = input().rstrip()
    t = 0
    print(is_pal(s), t)