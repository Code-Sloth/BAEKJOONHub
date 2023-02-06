import sys
input = sys.stdin.readline

s = input().rstrip()
s = s.replace(':-)','1')
s = s.replace(':-(','2')
s1 = s.count('1')
s2 = s.count('2')

if '1' not in s and '2' not in s: print('none')
else:
    if s1 == s2: print('unsure')
    elif s1 > s2: print('happy')
    else: print('sad')