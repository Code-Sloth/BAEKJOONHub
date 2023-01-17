t = int(input())
li = [0] * t
for i in range(t):
    li[i] = int(input())

for j in sorted(li):
    print(j)