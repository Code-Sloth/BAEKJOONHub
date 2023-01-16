t = int(input())

for i in range(t):
    total_a = 0
    total_b = 0
    for _ in range(9):
        a,b = map(int,input().split())
        total_a += a
        total_b += b
    if total_a > total_b:
        print('Yonsei')
    elif total_a < total_b:
        print('Korea')
    else:
        print('Draw')