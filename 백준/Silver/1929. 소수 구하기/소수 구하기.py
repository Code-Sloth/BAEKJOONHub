import sys
n1, n2 = map(int,sys.stdin.readline().split())
total = 0

for i in range(n1,n2+1):
    t = 0
    if i > 1:
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                t += 1
                if t > 0: break
        if t == 0:
            print(i)