for i in range(int(input())):
    a = list(input())
    t = 0
    tot = 0
    for j in a:
        if j == 'O':
            t += 1
            tot += t
        else:
            t = 0
    print(tot)