
import sys
input = sys.stdin.readline

li = input().split()
a, b = list(map(int,list(li[0]))), list(map(int,list(li[1])))

t = 0
if len(li[0]) > len(li[1]):
    for i in range(len(li[1])):
        t += b[i] * sum(a)
else:
    for i in range(len(li[0])):
        t += a[i] * sum(b)
print(t)