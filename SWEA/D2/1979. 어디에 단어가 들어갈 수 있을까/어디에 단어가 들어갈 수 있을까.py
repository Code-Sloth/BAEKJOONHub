for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    li = [list(input().split()) for _ in range(n)]
    li_T = [list(_) for _ in zip(*li)]

    total = 0
    for i in range(n):
        li[i] = ''.join(li[i])
        li_T[i] = ''.join(li_T[i])
        li[i] = li[i].split('0')
        li_T[i] = li_T[i].split('0')
        total += (li[i].count('1'*k) + li_T[i].count('1'*k))
        
    print(f'#{t}',total)