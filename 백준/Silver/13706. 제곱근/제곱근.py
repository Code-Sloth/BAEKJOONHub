import sys
input = sys.stdin.readline


n = int(input())
l = 0
r = n

while l <= r:
    m = (l+r)//2
    
    if m**2 == n:
        print(m)
        break
    elif m**2 < n:
        l = m + 1
    else:
        r = m - 1