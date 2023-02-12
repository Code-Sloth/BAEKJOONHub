import sys
input = sys.stdin.readline


from itertools import combinations

while 1:
    li = list(map(int,input().split()))
    n = li.pop(0)
    if n == 0: break
    comb = list(combinations(li,6))
    for i in comb:
        print(*sorted(i))
    print()