import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
li = [0] * n
li_q = [0] * n

for i in range(n):
    li[i] = i+1
q = deque(li)

for j in range(n):
    q.rotate(-(k-1))
    li_q[j] = str(q.popleft())

print(f'<{", ".join(li_q)}>')