import sys
input = sys.stdin.readline

t = 0
max_t = 0
for _ in range(4):
    o, i = map(int,input().split())
    t = t - o + i
    if t > max_t: max_t = t
print(max_t)