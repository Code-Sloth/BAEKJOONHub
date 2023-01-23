import sys

input = sys.stdin.readline

di = {}
for _ in range(int(input())):
    di[int(input())] = 0
for key in sorted(di.keys()):
    print(key)