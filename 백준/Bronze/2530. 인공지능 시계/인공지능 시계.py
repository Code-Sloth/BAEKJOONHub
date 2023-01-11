a,b,c=map(int,input().split())
d=int(input())

al = a*3600 + b*60 + c
ad = al + d
h = ad // 3600
m = ad % 3600 // 60
s = ad % 3600 % 60
print(h%24,m%60,s)