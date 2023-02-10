import math as mt

for t in range(1,int(input())+1):
    n = int(input())
    q = input().split()
    nn = mt.ceil(n/2)
    print(f'#{t}',end=' ')
    for i in range(nn):
        try:
            print(q[i],end=' ')
            print(q[i+nn],end=' ')
        except:break
    print()