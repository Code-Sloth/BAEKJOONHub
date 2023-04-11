import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = list(map(int,input().split()))

po = []
pi = []

for i in g:
    if i not in pi:
        if len(pi) >= n:
            pi.pop(po.index(min(po)))
            po.pop(po.index(min(po)))
        pi.append(i)
        po.append(1)
    else:
        po[pi.index(i)] += 1

print(' '.join(map(str,sorted(pi))))