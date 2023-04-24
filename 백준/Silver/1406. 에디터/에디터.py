import sys
input = sys.stdin.readline
from collections import deque

q = deque(list(input().rstrip()))
m = int(input())
c = len(q)
rota = 0

for _ in range(m):
    o = input().split()
    if o[0] == 'L' and c > 0:
        c -= 1
        q.rotate(1)
        rota -= 1
    elif o[0] == 'D' and c < len(q):
        c += 1
        q.rotate(-1)
        rota += 1
    elif o[0] == 'B' and c > 0:
        c -= 1
        q.pop()
    elif o[0] == 'P':
        c += 1
        q.append(o[1])

if rota > 0:
    for _ in range(rota):
        q.rotate(1) 
if rota < 0:
    for _ in range(-rota):
        q.rotate(-1)

print(''.join(q))