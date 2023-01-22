import sys

input = sys.stdin.readline

n = input()
is_create = False
for nn in range(int(n)):
    tot = nn
    nn = str(nn)
    for i in range(len(nn)):
        tot += int(nn[i])
    if tot == int(n):
        print(nn)
        is_create = True
        break
if is_create == False:
    print(0)