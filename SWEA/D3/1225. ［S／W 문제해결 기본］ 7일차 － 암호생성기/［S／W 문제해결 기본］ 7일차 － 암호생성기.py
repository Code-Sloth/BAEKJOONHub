from collections import deque

for _ in range(10):
    t = int(input())
    q = deque(list(map(int,input().split())))
    i = 1

    while 1:
        qq = q.popleft() - i
        if qq > 0:
            q.append(qq)
            if i < 5:
                i += 1
            else: i = 1
        else:
            q.append(0)
            break
    print(f'#{t}',*q)