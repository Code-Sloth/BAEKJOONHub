s = input().split(' ')
for i in range(s.count('')):
    s.remove('')
print(len(s))