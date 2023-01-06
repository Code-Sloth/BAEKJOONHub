c = int(input())


for i in range(c):
    li = list(map(int, input().split()))
    t = 0
    m = 0
    li2 = []

    avg = sum(li[1:])/li[0]
        
    for n in li[1:]:
        if n > avg:
            m += 1

    
    print(f'{m/li[0]*100:.3f}%')