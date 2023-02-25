import sys
input = sys.stdin.readline

n, m = map(int,input().split())
g1 = [list(map(int,input().split())) for _ in range(n)]

n2, m2 = map(int,input().split())
g2 = [list(map(int,input().split())) for _ in range(n2)]

li = [[] for _ in range(n)]

for i1 in range(n):
    for j2 in range(m2):
        t = 0
        for j1 in range(m):
            t += g1[i1][j1] * g2[j1][j2]
        li[i1].append(t)

for i in li:
    print(*i,end = '\n')
