import sys
input = sys.stdin.readline

from collections import deque
q = deque()
q_index = deque()

for _ in range(9):
    li = list(map(int,input().split()))
    q.append(max(li))
    q_index.append(li.index(max(li))+1)
print(max(q))
print(q.index(max(q))+1,q_index[q.index(max(q))])