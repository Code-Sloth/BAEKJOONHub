t = int(input())

for i in range(1,t+1):
    nums = list(map(int,input().split()))
    print(f'#{i} {round(sum(nums)/len(nums)):.0f}')