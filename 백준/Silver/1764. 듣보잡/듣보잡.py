import sys
input = sys.stdin.readline

a, b = map(int,input().split())
di = {}
li = []
t = 0

for _ in range(a+b):
    s = input().rstrip()
    if s not in di:
        di[s] = 1
    else:
        di[s] += 1
    if di[s] > 1:
        t += 1
        li.append(s)

print(t,*sorted(li),sep='\n')