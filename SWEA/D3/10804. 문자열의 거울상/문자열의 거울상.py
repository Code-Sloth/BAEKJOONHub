for t in range(1,int(input())+1):
    s = input()[::-1].strip()
    before = 'bdpq'
    after = 'dbqp'
    tr = str.maketrans(before,after)
    print(f'#{t} {s.translate(tr)}')