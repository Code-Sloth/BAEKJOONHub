import sys
input = sys.stdin.readline

n = int(input())

while n!=1: # n이 1이 될때까지 반복
    max_n = n # max_n = 72 ## max_n = 36 ## max_n = 18
    for i in range(1,n//2+1): # 1 2 3 4 ~~ 71 ## 1 2 3 4 ~~ 35
        if n % i == 0: # 나머지가 0, 약수를 찾는 조건
            max_n2 = i # max_n2 = 36 , i = 1 2 3 4 6 ~~ 36 ## max_n2 = 18
    n = max_n2 # n = 36 ## n = 18
    print(max_n // n) # 72 // 36 = 2 ## 36 // 18 = 2