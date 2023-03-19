import sys
input = sys.stdin.readline

a, b = input().split()

print(str(int(a[::-1]) + int(b[::-1].strip('0')))[::-1].strip('0'))