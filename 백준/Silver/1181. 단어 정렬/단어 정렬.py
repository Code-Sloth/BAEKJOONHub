import sys
input = sys.stdin.readline


li = []
di = {}

for _ in range(int(input())):
    li.append(input().strip())
li = sorted(li)

for i in li:
    di[i] = len(i)
print(*sorted(di.keys(),key = lambda x:di[x]),sep='\n')