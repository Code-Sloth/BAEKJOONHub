s = input()
t = 0

for i in s:
    if i == '@':
        t += 1
    elif i == '^':
        break
print(t,s.count('@')-t)