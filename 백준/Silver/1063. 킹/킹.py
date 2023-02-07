import sys
input = sys.stdin.readline

def move(kx,ky,bx,by,ord):
    dx,dy = di[ord]
    nx,ny = kx+dx, ky+dy
    if 0 <= nx+dx < 8 and 0 <= ny+dy < 8 and bx == nx and by == ny:
        bx,by = nx+dx, ny+dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        if bx != nx or by != ny:
            kx,ky = nx,ny
    return kx,ky,bx,by

tr = str.maketrans('ABCDEFGH','12345678')
tr_T = str.maketrans('12345678','ABCDEFGH')
tr_S = str.maketrans('01234567','87654321')
di = {'R':(0,1),'L':(0,-1),'B':(1,0),'T':(-1,0),
      'RT':(-1,1),'LT':(-1,-1),'RB':(1,1),'LB':(1,-1)}
k,b,n = input().split()
g = [[0]*8 for _ in range(8)]
k = k.translate(tr)
b = b.translate(tr)
kx,ky = 8-int(k[1]),int(k[0])-1
bx,by = 8-int(b[1]),int(b[0])-1

for _ in range(int(n)):
    order = input().rstrip()
    kx,ky,bx,by = move(kx,ky,bx,by,order)

k = str((ky+1)).translate(tr_T) + str(kx).translate(tr_S)
b = str((by+1)).translate(tr_T) + str(bx).translate(tr_S)
print(k,b)