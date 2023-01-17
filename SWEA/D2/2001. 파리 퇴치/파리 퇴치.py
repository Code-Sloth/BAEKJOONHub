for _ in range(1,int(input())+1):
    n, m = map(int,input().split())
    nums = []
    max_n = 0
    for nn in range(n):
        nums.append(list(map(int,input().split())))
    for i in range(n-m+1):
        for j in range(n-m+1):
            t = 0
            for k in range(m):
                for p in range(m):
                    t += nums[i+k][j+p]
            if t > max_n:
                max_n = t
    print(f'#{_} {max_n}')