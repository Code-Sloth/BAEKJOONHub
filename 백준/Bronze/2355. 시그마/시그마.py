a, b = map(int, input().split())
mxn = max(a, b)
mnn = min(a, b)
n = mxn - mnn
s = (n*(n+1)) // 2
print(s + (mnn * (n+1)))