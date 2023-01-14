t = int(input())

for _ in range(t):
    li = input().split()
    num = float(li[0])
    for i in li[1:]:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        elif i == '#':
            num -= 7
    print(f'{num:.2f}')