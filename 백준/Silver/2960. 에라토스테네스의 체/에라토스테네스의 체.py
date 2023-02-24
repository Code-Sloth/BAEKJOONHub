import sys
input = sys.stdin.readline

n,k = map(int,input().split())

def is_prime(n,k):
    li = [True] * (n+1)
    for i in range(2,n+1):
        if li[i]:
            for j in range(i, n+1, i):
                if li[j]:
                    k -= 1
                    li[j] = False
                    if not k: return j

print(is_prime(n,k))