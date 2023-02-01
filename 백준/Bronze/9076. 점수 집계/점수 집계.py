import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    li = deque(sorted(list(map(int,input().split())))[1:-1])
    if li[-1] - li[0] >= 4: print('KIN')
    else: print(sum(li))