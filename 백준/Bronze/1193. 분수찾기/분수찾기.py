import sys
input = sys.stdin.readline

n = int(input())

i = 0
while 1:
    i += 1
    if n <= (i*(i+1))//2:break

subtra = (i*(i+1))//2 - n + 1
if i % 2 != 0:
    print(f'{subtra}/{i+1-subtra}')
else:
    print(f'{i+1-subtra}/{subtra}')