li_x = []
li_y = []
for _ in range(3):
    a,b = map(int,input().split())
    li_x.append(a)
    li_y.append(b)

for i in li_x:
    if li_x.count(i) == 1:
        print(i,end=' ')
for j in li_y:
    if li_y.count(j) == 1:
        print(j)