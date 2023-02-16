import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
q = deque([i for i in range(1,n+1)])
li_q = [0] * n

for j in range(n):
    q.rotate(-(k-1))
    li_q[j] = q.popleft()

print('<',end='')
print(*li_q,sep=', ',end='>')