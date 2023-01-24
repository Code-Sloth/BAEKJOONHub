import sys
input = sys.stdin.readline

nums = [0] * 9
for i in range(9):
    nums[i] = int(input())
    
nums = sorted(nums)
sum_nums = sum(nums)-100
is_print = False

for i in range(8):
    for j in range(i+1,9):
        if sum_nums == nums[i] + nums[j]:
            for k in nums:
                if k != nums[i] and k != nums[j]:
                    print(k)
                    is_print = True
        if is_print == True:break
    if is_print == True:break