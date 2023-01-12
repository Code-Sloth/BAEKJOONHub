t = int(input())

for i in range(1,t+1):
    di = {}
    n = input() # 1259
    k = 0
    while 1:
        k += 1 # 1 2 3 4 5 6
        n2 = int(n)*k # 1259*1 1259*2 1259*3
        for j in str(n2): # '1' '2' '5' '9' '2' '5' '1' '8'
            di[int(j)] = 1
            num = n2
        if len(di) > 9:
            break
    print(f'#{i} {num}')