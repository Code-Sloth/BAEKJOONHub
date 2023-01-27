import sys
input = sys.stdin.readline

from collections import deque
q = deque()

if input().strip() == '고무오리 디버깅 시작':
    while 1:
        s = input().strip()
        if s == '고무오리 디버깅 끝':break
        elif s == '고무오리':
            if not q:
                q.append('문제')
                q.append('문제')
            else:q.pop()
        elif s == '문제':
            q.append(s)
    print('고무오리야 사랑해') if not q else print('힝구')