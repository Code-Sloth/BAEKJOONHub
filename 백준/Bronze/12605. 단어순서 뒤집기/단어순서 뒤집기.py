import sys
input = sys.stdin.readline

for t in range(1,int(input())+1):
    s = input().split()
    print(f'Case #{t}:',end=' ')
    print(*s[::-1])