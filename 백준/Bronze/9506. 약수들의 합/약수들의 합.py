while 1:
    n = int(input())
    if n == -1:
        break
    li = []
    s = f'{n} = {1}'
    for i in range(1,n):
        if n % i == 0:
            li.append(i)
    if sum(li) == n:
        for j in range(len(li)-1):
            s += f' + {li[j+1]}'
        print(s)
    else:
        print(f'{n} is NOT perfect.')