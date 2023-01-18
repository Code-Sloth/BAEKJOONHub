nums = list(map(int,input().split()))

while nums != sorted(nums):
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums.insert(i,nums[i+1])
            del nums[i+2]
            print(*nums)