n = int(input())
t = 0

for j in range(n):
    a = input() # aba
    t = 0
    for i in range(len(a)-1): # 0, 1
        if a[i] != a[i+1]:
            b = a[i+1:]
            if b.count(a[i]) > 0:
                t += 1
    if t > 0:
        n -= 1
print(n)