import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
li = []

for i in range(1,n-1):
    for j in range(i+1,n):
        li.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])

print(sorted(li)[0])