import sys
input = sys.stdin.readline

w, h = map(int,input().split())
n = int(input())

def dist(num, d):
    if num == 1: return 2*w + h - d
    if num == 2: return d
    if num == 3: return 2*w + h + d
    if num == 4: return w + h - d

g = []
for _ in range(n):
    num, d = map(int, input().split())
    g.append(dist(num, d))

dong_num, dong_d = map(int,input().split())
dong_d = dist(dong_num, dong_d)

result = 0
for i in range(n):
    clock = abs(dong_d - g[i])
    counter = 2*(w+h) - clock
    result += min(clock, counter)

print(result)