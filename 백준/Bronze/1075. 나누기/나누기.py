n = input()
f = int(input())
a = int(n[:-2] + '00')
while 1:
    if a % f == 0:
        break
    a += 1
print(str(a)[-2:])