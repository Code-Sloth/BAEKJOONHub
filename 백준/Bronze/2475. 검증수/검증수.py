nums = list(input().split())
t = 0
for i in nums:
    t += int(i)**2
print(t%10)