a = int(input())
for k in range(a):
    num, s = input().split()
    for j in s:
        print(j*int(num),end='')
    print()