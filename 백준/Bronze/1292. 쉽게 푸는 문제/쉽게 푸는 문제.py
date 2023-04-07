import sys
input = sys.stdin.readline

a,b=map(int,input().split())
g=[0]
sum=0

for i in range(1,b+1):
  for j in range(i):
    g.append(i)

for i in range(a, b+1):
  sum+=g[i]
print(sum)