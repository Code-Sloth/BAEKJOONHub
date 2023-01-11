a,b,c = map(int,input().split())
di = dict.fromkeys(range(1,101),0)

for i in range(3):
    inn,away = map(int,input().split())
    for j in range(inn,away):
        di[j] += 1

t = 0
for k in di.values():
    if k == 1:
        t += a
    elif k == 2:
        t += b * 2
    elif k == 3:
        t += c * 3

print(t)