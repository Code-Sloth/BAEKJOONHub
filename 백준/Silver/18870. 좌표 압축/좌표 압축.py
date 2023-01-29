import sys
input = sys.stdin.readline


n = int(input())
li = list(map(int,input().split()))
li2 = sorted(list(set(li)))
di = {li2[i] : i for i in range(len(li2))}

for i in li:
    print(di[i], end = ' ')