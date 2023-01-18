for _ in range(int(input())):
    floor = int(input())
    n = int(input())
    li = list(range(1,n+1))
    li2 = [0] * n
    li2[0] += 1
    
    for j in range(floor):
        for i in range(1,n):
            li2[i] = sum(li[:i+1])
        li = li2.copy()
    print(li[n-1])