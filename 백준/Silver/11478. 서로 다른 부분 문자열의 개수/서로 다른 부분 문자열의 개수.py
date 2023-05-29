import sys
input = sys.stdin.readline

s = input().rstrip()
se = set()
len_s = len(s)

for i in range(len_s):
    for j in range(i, len_s):
        substring = s[i:j+1]
        se.add(substring)

print(len(se))