import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

print(len(a^b))