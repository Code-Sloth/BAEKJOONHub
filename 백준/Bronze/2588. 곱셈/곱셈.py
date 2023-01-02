a=int(input())
b=int(input())
c=b%10
d=(b-(b//100)*100)//10
e=b//100
print(a*c,a*d,a*e,a*b,sep='\n')