nums = list(map(int,input().split()))
money = 0

for i in nums:
    if nums.count(i) == 3:
        money = 10000 + i * 1000
        break
    elif nums.count(i) == 2:
        money = 1000 + i * 100
        break
    else:
        money = max(nums) * 100

print(money)