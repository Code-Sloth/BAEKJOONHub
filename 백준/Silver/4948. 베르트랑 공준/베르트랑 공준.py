import sys
input = sys.stdin.readline

import bisect
def is_prime(n):
    li = [True] * n
    
    for i in range(2,int(n**0.5)+1):
        if li[i] == True:
            for j in range(2*i, n, i):
                li[j] = False
    return [num for num in range(2,n) if li[num] == True]
li = is_prime(123456 * 2)
while 1:
    n = int(input())
    if n == 0: break
    print(bisect.bisect(li, 2 * n) - bisect.bisect(li, n))