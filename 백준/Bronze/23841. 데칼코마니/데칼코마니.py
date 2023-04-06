import sys
input = sys.stdin.readline

n,m=map(int,input().split())
g=[]
for i in range(n):
    li=list(input())
    for j in range(m//2):
        if li[j]!='.':
            li[m-j-1]=li[j]
        elif li[m-j-1]!='.':
            li[j]=li[m-j-1]
    g.append(li)
    
for i in range(len(g)):
    for j in range(len(g[i])):
        print(g[i][j],end="")