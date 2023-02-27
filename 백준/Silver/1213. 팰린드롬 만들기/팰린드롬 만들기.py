import sys
input = sys.stdin.readline

q = sorted(list(input().rstrip()),reverse=True)
s = ''
last = ''
t = 0

for i in q[::-1]:
    cnt = q.count(i)
    if cnt % 2 == 1:
        t += 1
        last = i
        s += i * (cnt//2)
        for _ in range(cnt): q.pop()
    elif cnt % 2 == 0:
        s += i * (cnt//2)
        for _ in range(cnt): q.pop()
    if t > 1: print("I'm Sorry Hansoo"); sys.exit()

s += last

if not t:
    s += s[::-1]
else:
    s += s[-2::-1]
print(s)