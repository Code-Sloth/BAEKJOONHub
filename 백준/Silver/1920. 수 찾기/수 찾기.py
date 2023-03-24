import sys
input = sys.stdin.readline

n = int(input())
g = sorted(list(map(int,input().split())))
m = int(input())
mg = list(map(int,input().split()))

def func(a):
    st = 0
    ed = n-1

    while st <= ed:
        mid = (st+ed) // 2
        if g[mid] == a:
            return 1
        elif g[mid] < a:
            st = mid + 1
        else:
            ed = mid - 1

for i in mg:
    if func(i):
        print(1)
    else:
        print(0)