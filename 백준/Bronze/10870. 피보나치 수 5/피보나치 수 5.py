n = int(input())

di = {0:0,1:1}
def f(n):
    if n in di: return n
    else: return f(n-2) + f(n-1)
print(f(n))