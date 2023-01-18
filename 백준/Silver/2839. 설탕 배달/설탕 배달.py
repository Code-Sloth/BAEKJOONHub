n = int(input())
sol = 0

for three in range(n):
    for five in range(n):
        if 5 * five + 3 * three == n:
            sol += (five + three)
    if sol > 0:
        print(sol)
        break
if sol == 0:
    print(-1)