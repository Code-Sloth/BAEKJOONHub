import sys
input = sys.stdin.readline

n, k = map(int,input().split())
li = [list(map(int,input().split())) for i in range(n)]
li2 = sorted(li,key = lambda x : (x[1],x[2],x[3]),reverse = True)
t = 1

for i in range(1,len(li2)+1):
    try:
        if li2[i][1:] != li2[i-1][1:]:
            t += 1
        if li2[i][0] == k:break
    except:
        t = 1
print(t)