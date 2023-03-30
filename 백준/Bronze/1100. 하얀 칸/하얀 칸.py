import sys
input = sys.stdin.readline

g = [list(map(str,list(input()))) for _ in range(8)]

t = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            if g[i][j] == 'F': #F있을 경우
                t += 1
print(t)