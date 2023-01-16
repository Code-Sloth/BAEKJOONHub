li = [0,0,0,0,0]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a>0 and b>0:
        li[0] += 1
    elif a<0 and b>0:
        li[1] += 1
    elif a<0 and b<0:
        li[2] += 1
    elif a>0 and b<0:
        li[3] += 1
    else:
        li[4] += 1
print(f'Q1: {li[0]}\nQ2: {li[1]}\nQ3: {li[2]}\nQ4: {li[3]}\nAXIS: {li[4]}')