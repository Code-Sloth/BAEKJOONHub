n,x=map(int,input().split())
a=list(map(int,input().split()))

for i in a:
    if i>=x:
        continue
    print(i,end=' ')