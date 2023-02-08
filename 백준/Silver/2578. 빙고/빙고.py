import sys
input = sys.stdin.readline

g = [list(map(int,input().split())) for _ in range(5)]
order = [list(map(int,input().split())) for _ in range(5)]
di = {}

for i in range(5):
    for j in range(5):
        di[g[i][j]] = i,j

l = [0] * 12
t = 0
for ord in order:
    for i in range(5):
        b = di[ord[i]]
        t += 1
        if b[0] == b[1]: l[0] += 1
        if b[0] + b[1] == 4: l[1] += 1
        if b[0] == 0: l[2] += 1
        if b[0] == 1: l[3] += 1
        if b[0] == 2: l[4] += 1
        if b[0] == 3: l[5] += 1
        if b[0] == 4: l[6] += 1
        if b[1] == 0: l[7] += 1
        if b[1] == 1: l[8] += 1
        if b[1] == 2: l[9] += 1
        if b[1] == 3: l[10] += 1
        if b[1] == 4: l[11] += 1
        if l.count(5) > 2:
            print(t)
            exit()