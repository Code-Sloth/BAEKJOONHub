import sys
n = int(sys.stdin.readline())
n2 = 1
t = 0

while n > t:
    n2 += 1
    if n2 % 2 == 0:
        for i in range(1,n2):
            cnt1 = n2-i
            cnt2 = i
            t += 1
            if n == t:
                break
    else:
        for j in range(1,n2):
            cnt1 = j
            cnt2 = n2-j
            t += 1
            if n == t:
                break

print(f'{cnt1}/{cnt2}')