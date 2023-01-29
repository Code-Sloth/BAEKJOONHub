import sys
input = sys.stdin.readline

li = [list(map(int,input().split())) for x in range(int(input()))]
for i in sorted(sorted(li,key = lambda x : x[0]),key = lambda x : x[1]):
    print(*i)