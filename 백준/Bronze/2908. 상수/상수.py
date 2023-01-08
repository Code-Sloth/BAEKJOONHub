a, b = input().split()

a2 = a[::-1]
b2 = b[::-1]

if int(a2) > int(b2):
    print(a2)
else:
    print(b2)