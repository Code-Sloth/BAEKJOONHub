import sys
input = sys.stdin.readline
import math

for _ in range(int(input())):
    li = list(map(int,input().split()))
    r_pl = li[2] + li[5]                
    r_mi = abs(li[2]-li[5])
    d = math.sqrt(abs(li[0]-li[3])**2+abs(li[1]-li[4])**2)
   
    if r_mi < d < r_pl: print(2)
    elif d != 0 and r_mi == d or r_pl == d: print(1)
    elif r_mi > d or r_pl < d or (d == 0 and li[2] != li[5]): print(0)
    else:print(-1)