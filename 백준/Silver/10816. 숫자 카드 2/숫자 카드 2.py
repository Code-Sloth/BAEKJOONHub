import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
ng = Counter(list(map(int,input().split())))
m = int(input())
mg = list(map(int,input().split()))

result = []
for i in mg:
    result.append(ng[i])

print(*result)