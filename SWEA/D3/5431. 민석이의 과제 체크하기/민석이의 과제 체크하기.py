for t in range(1, int(input())+1):
    n, k = map(int,input().split())
    li = list(map(int,input().split()))
    li2 = []
    for i in range(1,n+1):
        if i not in li:
            li2.append(i)
    print(f'#{t}',*li2)