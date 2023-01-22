import sys

input = sys.stdin.readline

while 1:
    n = input().strip()
    if n == '0':break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')