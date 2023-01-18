s = input()
camb = 'CAMBRIDGE'
for i in s:
    if i in camb:
        s = s.replace(i,'')
print(s)