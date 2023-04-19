import sys
input = sys.stdin.readline

from collections import deque

g =[deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())
for _ in range(k):
    i, d = map(int,input().split())
    i -= 1
    li = [-1] * 4
    li[i] = d
    j = i
    cd = d

    while i < 3 or j > 0:
        if i < 3:
            if li[i] and g[i][2] != g[i+1][-2]:
                d = -d
                li[i+1] = d
            else: li[i+1] = 0
        if j > 0:
            if li[j] and g[j][-2] != g[j-1][2]:
                cd = -cd
                li[j-1] = cd
            else: li[j-1] = 0
        i += 1
        j -= 1
    
    for i in range(4):
        if li[i]:
            g[i].rotate(li[i])


print(g[0][0]*1 + g[1][0]*2 + g[2][0]*4 + g[3][0]*8)