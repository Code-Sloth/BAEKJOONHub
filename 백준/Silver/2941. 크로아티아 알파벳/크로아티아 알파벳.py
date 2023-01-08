li = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = list(input())
t=0
le = len(s)

for i in range(1,len(s)):
    if s[i-1] + s[i] in li:
        t += 1
        le -= 2
for j in range(2,len(s)):
    if s[j-2] + s[j-1] + s[j] in li:
        t += 1
        le -= 3
        if s[j-2] == 'd':
            le += 1
print(t+le)