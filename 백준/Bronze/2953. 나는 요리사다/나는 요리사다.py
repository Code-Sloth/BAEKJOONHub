import sys
input = sys.stdin.readline

li = [sum(list(map(int,input().split()))) for _ in range(5)]
print(li.index(max(li))+1,max(li))