li = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        li.append(n)
if li == []:
    print(-1)
else:
    print(sum(li),min(li),sep = '\n')