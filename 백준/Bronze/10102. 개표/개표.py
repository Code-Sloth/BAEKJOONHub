v = int(input())

li = list(input())
if li.count('A') > v//2:
    print('A')
elif li.count('B') > v//2:
    print('B')
else:
    print('Tie')