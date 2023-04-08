import sys
input = sys.stdin.readline

g = list(map(int, input().split()))

def func(n):
    min = int(''.join(map(str, n)))
    for i in range(1,4):
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    return min

num = func(g)
cnt = 1

for i in range(1111, num):
    if '0' not in list(str(i)) and i == func(list(map(int, str(i)))):
        cnt += 1
print(cnt)