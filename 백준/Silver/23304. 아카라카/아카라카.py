import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

s = input().rstrip()

def aka(s):
    if len(s) == 1: return 1
    l = s[0:len(s)//2]
    r = s[(len(s)+1)//2:len(s)]
    if l != r[::-1]: return 0
    if not aka(l) or not aka(r): return 0
    else: return 1

if aka(s): print('AKARAKA')
else: print('IPSELENTI')