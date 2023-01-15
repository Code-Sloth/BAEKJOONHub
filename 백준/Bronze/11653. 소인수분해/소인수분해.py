n = int(input())
nums = ''

try:
    while 1:
        max_n = n
        for i in range(1,n):
            if n % i == 0:
                max_n2 = i
        n = max_n2
        if n == 1:
            nums += (str(max_n)+' ')
            break
        else:
            nums += (str(max_n // n)+' ')
    print(*nums.split(),sep='\n')
except:
    print()