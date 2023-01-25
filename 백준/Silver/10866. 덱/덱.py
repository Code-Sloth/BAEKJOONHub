import sys
input = sys.stdin.readline

from collections import deque
q = deque()

def push_front(x):
    q.appendleft(x)
def push_back(x):
    q.append(x)
def pop_front():
    return q.popleft() if q else -1
def pop_back():
    return q.pop() if q else -1
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
    if ord == 'push_front':
        push_front(order[1])
    if ord == 'push_back':
        push_back(order[1])
    if ord == 'pop_front':
        print(pop_front())
    if ord == 'pop_back':
        print(pop_back())
    if ord == 'size':
        print(size())
    if ord == 'empty':
        print(empty())
    if ord == 'front':
        print(front())
    if ord == 'back':
        print(back())