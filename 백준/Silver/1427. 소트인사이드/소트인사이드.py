import sys
input = sys.stdin.readline

s = input().strip()
for i in sorted(s,reverse=True):
    print(i,end='')