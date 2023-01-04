n=0
max=0
for i in range(9):
    a = int(input())
    n += 1
    if a > max:
        max = a
        m = n

print(f'{max}\n{m}')