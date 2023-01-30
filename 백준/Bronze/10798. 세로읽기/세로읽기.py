import sys
input = sys.stdin.readline

li = [list(input().strip()) for i in range(5)]
max_li = max(map(len,li))

for i in range(max_li):
    for j in range(5):
        try:
            print(li[j][i],end='')
        except:pass