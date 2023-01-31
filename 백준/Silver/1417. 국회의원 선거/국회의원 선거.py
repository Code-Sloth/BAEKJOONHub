import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
if n == 1:print(0)
else:
    t = 0
    while 1:
        li = [li[0]] + sorted(li[1:],reverse=True)
        if li[0] <= li[1]:
            li[1] -= 1
            li[0] += 1
            t += 1
        if li[0] == max(li) and li[0] not in li[1:]:break
    print(t)