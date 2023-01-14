li = []
for _ in range(3):
    li.append(input())

if li[1] == '*':
    print(int(li[0]) * int(li[2]))
elif li[1] == '+':
    print(int(li[0]) + int(li[2]))