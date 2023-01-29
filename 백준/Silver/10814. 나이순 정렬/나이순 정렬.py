import sys
input = sys.stdin.readline


li = [list(input().split()) for x in range(int(input()))]
for i in li:
    i[0] = int(i[0])

for i in sorted(li,key = lambda x : x[0]):
    print(*i)