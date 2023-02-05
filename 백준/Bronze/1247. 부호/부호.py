import sys
input = sys.stdin.readline

for _ in range(3):
    t = 0
    for __ in range(int(input())):
        t += int(input())
    if t > 0:print('+')
    elif t == 0: print(0)
    else:print('-')