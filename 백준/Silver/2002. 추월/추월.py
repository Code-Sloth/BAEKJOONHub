import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

in_car = deque()
t = 0
for i in range(2*n):
    if i < n:
        in_car.append(input().rstrip())
    else:
        out_car = input().rstrip()

        if out_car != in_car[0]:
            t += 1
        in_car.remove(out_car)

print(t)