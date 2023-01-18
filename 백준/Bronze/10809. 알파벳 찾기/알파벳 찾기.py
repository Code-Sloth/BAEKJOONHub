import string

low = list(string.ascii_lowercase)
s = input()

for i in low:
    print(s.find(i),end=' ')