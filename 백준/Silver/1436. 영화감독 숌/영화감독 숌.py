import sys
input = sys.stdin.readline

n = 666
i = 0
num = int(input()) - 1
while 1:
    if '666' in str(n):
        if num == i:
            print(n)
            break
        i += 1
    n += 1