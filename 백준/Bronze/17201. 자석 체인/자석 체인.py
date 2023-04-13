import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print('No')
        sys.exit()
else:
    print('Yes')