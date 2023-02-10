n = int(input())

di = {0:1,1:1}
def f(n):
    if n in di: return di[n]
    else: return n * f(n-1)
print(f(n))