n = int(input())
ns = list(map(int,input().split()))
total = 0

for i in ns:
    t = 0
    for j in range(1,i):
        if i % j == 0:
            t += 1
    if t == 1:
        total += 1
print(total)