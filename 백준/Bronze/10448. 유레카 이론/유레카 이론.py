import sys
input = sys.stdin.readline

li = [0] * 45
for i in range(1,46):
    li[i-1] = i*(i+1)//2

for _ in range(int(input())):
    n = int(input())
    is_T = False
    for i in range(45):
        for j in range(45):
            for k in range(45):
                if li[i] + li[j] + li[k] == n:
                    is_T = True
                    break
            if is_T == True:break
        if is_T == True:break
    print(int(is_T))