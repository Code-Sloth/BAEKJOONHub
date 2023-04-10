import sys
input = sys.stdin.readline

n = int(input())
pal = input().split()
g = set()

for i in range(n):
    g.add(pal[i][0])

if len(g) == 1:
    print(1)
else:
    print(0)