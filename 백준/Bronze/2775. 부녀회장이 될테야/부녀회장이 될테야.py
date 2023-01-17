for _ in range(int(input())):
    k = int(input())
    n = int(input())
    li = list(range(1,n+1))
    li2 = [0] * n
    li2[0] += 1
    li3 = li.copy()
    for j in range(k):
        for i in range(1,n):
            li2[i] = sum(li3[:i+1])
        li3 = li2.copy()
    print(li3[n-1])