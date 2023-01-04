a=int(input())
b=list(map(int,input().split()))
c=int(input())
n=0

for i in b:
    if c==i:
        n += 1

print(n)