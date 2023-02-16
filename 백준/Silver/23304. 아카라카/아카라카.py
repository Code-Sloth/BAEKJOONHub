import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

s = input().rstrip()

def aka(s):
    if len(s) == 1: return 1
    l = s[0:len(s)//2]
    r = s[(len(s)+1)//2:len(s)]
    if l != r[::-1]:
        print('IPSELENTI')
        sys.exit()
    if not aka(l):
        print('IPSELENTI')
        sys.exit()
    else: return 1

if aka(s): print('AKARAKA')