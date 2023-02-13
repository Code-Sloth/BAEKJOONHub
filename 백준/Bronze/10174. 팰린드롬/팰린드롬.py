import sys
input = sys.stdin.readline
import string

ABC = string.ascii_uppercase
abc = string.ascii_lowercase
tr = str.maketrans(ABC,abc)

def pal(s):
    if s != s[::-1]: return 'No'
    else: return 'Yes'

for i in range(int(input())):
    s = input().strip()
    s = s.translate(tr)
    print(pal(s))