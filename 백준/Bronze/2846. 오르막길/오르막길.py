t = int(input())
nums = list(map(int,input().split()))

li = []
max_li = 0
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        li.append(nums[i])
        li.append(nums[i+1])
        if max(li)-min(li) > max_li:
            max_li = max(li)-min(li)
    if nums[i] >= nums[i+1]:
        li.clear()

print(max_li)