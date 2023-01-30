import sys
input = sys.stdin.readline

li = input().split()
print(sum(map(int,li[0]))*sum(map(int,li[1])))