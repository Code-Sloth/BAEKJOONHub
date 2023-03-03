import sys
input = sys.stdin.readline

s = input().rstrip()
result = ''

t = 0
for i in range(len(s)):
    if s[i] == 'X':
        t += 1
    else:
        if t % 2 == 1:
            print(-1)
            sys.exit()
        t = 0
        result += '.'
    if i == len(s)-1 and t % 2 == 1 and s[i] == 'X':
        print(-1)
        sys.exit()
    if t == 2:
        result += 'BB'
    elif t == 4:
        result = result[:-2] + result[-2:].replace('B','A')
        result += 'AA'
        t = 0

print(result)