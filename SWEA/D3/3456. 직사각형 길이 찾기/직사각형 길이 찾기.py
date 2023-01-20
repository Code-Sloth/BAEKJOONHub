for t in range(1,int(input())+1):
    li = list(map(int,input().split()))
    for i in li:
        if li.count(i) == 1 or li.count(i) == 3:
            print(f'#{t} {i}')
            break