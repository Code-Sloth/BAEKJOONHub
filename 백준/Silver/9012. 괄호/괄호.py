import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()

    if len(s) % 2 == 1:print('NO')

    while len(s) % 2 == 0:
        if '()' in s:
            s = s.replace('()','')
        else:
            print('NO')
            break
        if len(s) == 0:
            print('YES')
            break