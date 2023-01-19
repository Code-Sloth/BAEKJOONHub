di = {}
for _ in range(int(input())):
    a,b = input().split()
    di[a] = b
di2 = di.copy()

for i in di2:
    if di2[i] == 'leave':
        del di[i]

print(*sorted(di.keys(),reverse=True),sep='\n')