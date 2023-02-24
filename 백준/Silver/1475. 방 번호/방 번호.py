import sys
input = sys.stdin.readline

li = list(input().rstrip())

max_li = 0
for i in range(10):
    if i == 6 or i == 9:
        max_li = max(max_li,(li.count('6')+li.count('9')+1)//2)
    else:
        max_li = max(max_li,li.count(str(i)))

print(max_li)