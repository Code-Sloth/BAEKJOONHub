import sys
input = sys.stdin.readline

from collections import deque
while 1:
    try:
        s, t = input().split()
        q = deque([i for i in s])
        for i in t:
            if q and i == q[0]:
                q.popleft()
        print('No') if q else print('Yes')
    except:break