import sys
input = sys.stdin.readline

s = input().rstrip()
s1 = s.count(':-)')
s2 = s.count(':-(')

if ':-)' not in s and ':-(' not in s: print('none')
else:
    if s1 == s2: print('unsure')
    elif s1 > s2: print('happy')
    else: print('sad')