import sys
input = sys.stdin.readline

n, d, k, c = map(int, sys.stdin.readline().split())
g = {i : int(input()) for i in range(n)}
st = result = 0

while st != n:
    li = set()
    coupon = True
    for i in range(st, st+k):
        i %= n
        li.add(g[i])
        if g[i] == c:
            coupon = False

    cnt = len(li)
    if coupon:
        cnt += 1
    result = max(result, cnt)
    st += 1

print(result)