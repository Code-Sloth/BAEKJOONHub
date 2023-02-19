import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

t = 1
while 1:
    if a==b==c==1:
        print(t)
        break
    a,b,c = a-1,b-1,c-1
    if a < 1: a = 15
    if b < 1: b = 28
    if c < 1: c = 19
    t += 1
