import math
for _ in range(int(input())):
    h,w,n = map(int,input().split())
    if n % h == 0:
        num_1 = h
    else:
        num_1 = n % h
    num_2 = math.ceil(n / h)
    if num_2 < 10:
        num_2 = '0' + str(num_2)
    print(str(num_1) + str(num_2))