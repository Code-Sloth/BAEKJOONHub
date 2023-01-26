import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    while '()' in s:
        s = s.replace('()','')
    print('NO') if s else print('YES')