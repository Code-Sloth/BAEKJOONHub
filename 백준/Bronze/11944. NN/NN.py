N, M = map(int, input().split())
res = str(N)*N
print(res if len(res) <= M else res[:M])