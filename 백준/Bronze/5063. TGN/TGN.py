n = int(input())

for i in range(n):
    r,e,c = map(int,input().split())
    if r+c < e:
        print('advertise')
    elif r+c > e:
        print('do not advertise')
    else:
        print('does not matter')