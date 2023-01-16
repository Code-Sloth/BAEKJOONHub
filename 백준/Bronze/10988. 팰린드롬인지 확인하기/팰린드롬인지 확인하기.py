s = input()
t = 0
for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        t += 1
if t == len(s)//2:
    print(1)
else:
    print(0)