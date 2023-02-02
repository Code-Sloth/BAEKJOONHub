import sys
input = sys.stdin.readline

ball = 1
for _ in range(int(input())):
    a,b = map(int,input().split())
    if ball == a:ball = b
    elif ball == b:ball = a
print(ball)