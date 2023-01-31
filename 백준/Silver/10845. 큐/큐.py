import sys
input = sys.stdin.readline

from collections import deque
q = deque()

def push(x):
    q.append(x)
def pop():
    return q.popleft() if q else -1
def size():
    return len(q)
def empty():
    return 1 if not q else 0
def front():
    return q[0] if q else -1
def back():
    return q[-1] if q else -1

for _ in range(int(input())):
    order = input().split()
    ord = order[0]
    if ord == 'push':push(order[1])
    elif ord == 'pop':print(pop())
    elif ord == 'size':print(size())
    elif ord == 'empty':print(empty())
    elif ord == 'front':print(front())
    else:print(back())