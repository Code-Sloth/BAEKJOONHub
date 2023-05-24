import sys
input = sys.stdin.readline

g = list(input())
zero, one = g.count('0')//2, g.count('1')//2
print('0'*zero + '1'*one)