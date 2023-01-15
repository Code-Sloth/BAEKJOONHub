s = int(input())
t = 0
n = 0

for i in range(1,s+1):
    t += i
    n += 1
    if t == s:
        print(n)
        break
    if t > s:
        print(n-1)
        break