li = ['a','e','i','o','u']
for t in range(1,int(input())+1):
    s = input().rstrip()
    print(f'#{t}',end=' ')
    for i in s:
        if i not in li:
            print(i,end='')
    print()