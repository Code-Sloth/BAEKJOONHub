import sys
input = sys.stdin.readline

a, b = map(int,input().split())
q = []
q.append(abs(a-b))

for _ in range(int(input())):
    n = int(input())
    q.append(abs(b-n)+1)

print(min(q))