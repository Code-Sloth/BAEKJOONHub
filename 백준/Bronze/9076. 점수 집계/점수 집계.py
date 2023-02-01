for _ in range(int(input())):
    li = sorted(list(map(int,input().split())))
    print(sum(li[1:4]) if li[3]-li[1] < 4 else 'KIN')