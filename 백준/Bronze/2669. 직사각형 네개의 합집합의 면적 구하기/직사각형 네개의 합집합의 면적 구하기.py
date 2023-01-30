import sys
input = sys.stdin.readline

xy = [[0] * 101 for i in range(101)]
for _ in range(4):
    li = list(map(int,input().split()))
    for x in range(li[0],li[2]):
        for y in range(li[1],li[3]):
            xy[x][y] = 1

print(sum(map(sum,xy)))