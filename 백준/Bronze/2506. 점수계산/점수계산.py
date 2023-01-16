total_point = 0
point = 0
n = int(input())

for i in list(map(int,input().split())):
    if i == 0:
        point = 0
    else:
        point += 1
        total_point += point
print(total_point)