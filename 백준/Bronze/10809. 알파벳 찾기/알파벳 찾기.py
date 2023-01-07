import string
s = input()

abc = string.ascii_lowercase
abc_li = []
abc_li.extend(abc)

for i in abc_li:
    print(s.find(i),end=' ')