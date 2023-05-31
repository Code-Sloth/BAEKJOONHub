import sys
input = sys.stdin.readline

i = 0
while 1:
    i += 1
    s = input().rstrip()
    if '-' in s: break

    scount, t = 0, 0
    for st in s:
        if st == '{':
            scount += 1
        else:
            if scount:
                scount -= 1
            else:
                t += 1
                scount += 1
    print(f'{i}. {t + scount//2}')