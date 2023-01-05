a=int(input())
b=list(map(int,input().split()))
c=0

for i in b:
    c+=i/max(b)*100
    
print(c/a)