t = int(input())
nums = list(map(int,input().split()))

max_li = []
j = 0
for i in range(t-1):
    if nums[i] >= nums[i+1]:
        max_li.append(max(nums[j:i+1])-min(nums[j:i+1]))
        j = i+1
    elif i == t-2 and nums[i] < nums[i+1]:
        max_li.append(max(nums[j:])-min(nums[j:]))
print(max(max_li))