import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    order = list(input().split())
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if stack == []:print(-1)
        else:print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack == []:print(1)
        else:print(0)
    elif order[0] == 'top':
        if stack != []:print(stack[len(stack)-1])
        else:print(-1)
