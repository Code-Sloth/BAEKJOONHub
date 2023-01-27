import sys
input = sys.stdin.readline

n, m = map(int,input().split())

li_a = set([input().strip() for _ in range(n)])
li_b = [input().strip() for __ in range(m)]

t = 0
for i in li_b:
    if i in li_a:
        t += 1
print(t)