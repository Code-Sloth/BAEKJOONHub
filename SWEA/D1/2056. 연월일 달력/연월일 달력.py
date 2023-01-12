li=[]
for k in range(1,13):
    if k == 2:
        li.append(range(1,29))
    elif k==4 or k==6 or k==9 or k==11:
        li.append(range(1,31))
    else:
        li.append(range(1,32))
    

for i in range(1,int(input())+1):
    n = input()
    if int(n[4:6]) == 0 or int(n[4:6]) > 12:
        print(f'#{i} -1')
    else:
        if int(n[6:8]) in li[int(n[4:6])-1]:
            print(f'#{i} {n[:4]}/{n[4:6]}/{n[6:8]}')
        else:
            print(f'#{i} -1')