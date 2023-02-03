paren = ['()','[]','{}','<>']

for t in range(1,11):
    ls = int(input())
    s = input().strip()

    while 1:
        for i in paren:
            s = s.replace(i,'')
        if '()' not in s and '[]' not in s and '{}' not in s and '<>' not in s:break
    
    print(f'#{t}', 0) if s else print(f'#{t}', 1)