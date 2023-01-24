import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
li = [0] * n
li_q = [0] * n
q = deque()

for i in range(1,n+1):
    q.append(i)

for j in range(n):
    q.rotate(-(k-1))
    li_q[j] = str(q.popleft())

print(f'<{", ".join(li_q)}>')