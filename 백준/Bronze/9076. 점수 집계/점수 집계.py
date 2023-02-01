for _ in range(int(input())):
    li = sorted(list(map(int,input().split())))[1:-1]
    if li[-1] - li[0] >= 4: print('KIN')
    else: print(sum(li))