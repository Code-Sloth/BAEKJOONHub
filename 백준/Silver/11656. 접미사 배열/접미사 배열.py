import sys
input = sys.stdin.readline

s = input().rstrip()
q = []

for i in range(len(s)):
    q.append(s[i:])

q.sort()

for _ in range(len(s)):
    print(q[_])