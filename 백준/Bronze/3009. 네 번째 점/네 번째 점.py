aa,bb = [0]*3,[0]*3
for i in range(3):
    a,b = map(int,input().split())
    aa[i] = a
    bb[i] = b

for aaa in aa:
    if aa.count(aaa) == 1:
        print(aaa,end=' ')
for bbb in bb:
    if bb.count(bbb) == 1:
        print(bbb)