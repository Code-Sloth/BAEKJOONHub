import sys
input = sys.stdin.readline

n = int(input())


for i in range(4473):
    if n <= (i*(i+1))//2:
        bn = i + 1
        break

subtra = (bn*(bn-1))//2 - n + 1
if (bn - 1) % 2 != 0:
    print(f'{subtra}/{bn-subtra}')
else:
    print(f'{bn-subtra}/{subtra}')