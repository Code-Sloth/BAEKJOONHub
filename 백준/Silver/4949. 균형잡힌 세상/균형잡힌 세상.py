import sys
input = sys.stdin.readline

while True:
    a = input()
    if a[0] == '.':
        break
    c = 'yes'
    stack = []
    for i in a:
        if i == '(' or  i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                t = stack.pop()
                if t != '(':
                    c = 'no'
                    break
            else:
                c = 'no'
                break
        elif i == ']':
            if stack:
                t = stack.pop()
                if t != '[':
                    c = 'no'
                    break
            else:
                c = 'no'
                break
    if stack:
        c = 'no'
    print(c)