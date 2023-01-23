import sys

input = sys.stdin.readline

a,b = map(int,input().split())
c=a
d=b
while b>0:
    a,b=b,a%b
print(a,a*(c//a)*(d//a),sep='\n')