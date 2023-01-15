n = int(input())

while n!=1:
    max_n = n
    for i in range(1,n):
        if n % i == 0:
            max_n2 = i
    n = max_n2
    print(max_n // n)
