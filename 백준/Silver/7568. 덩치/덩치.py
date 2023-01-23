import sys

input = sys.stdin.readline

n = int(input())
li = [None] * n
li_nd = 0

for i in range(n):
    a,b = map(int,input().split())
    li[i] = [a,b]

for j in li:
    t = 1
    for k in range(n):
        if k == li.index(j):continue
        if j[0] < li[k][0] and j[1] < li[k][1]:
            t += 1
    print(t,end=' ')