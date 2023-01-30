import sys
input = sys.stdin.readline

li = [list(input().strip()) for i in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(li[j][i],end='')
        except:pass