aa,bb=0,0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a < b:
        aa += b
    elif a > b:
        bb += a
print(100-aa,100-bb,sep='\n')