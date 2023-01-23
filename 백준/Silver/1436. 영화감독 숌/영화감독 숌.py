import sys

input = sys.stdin.readline

n = 665
li = [0] * 10001
i = 0
num = int(input())-1
while 1:
    n += 1
    st_n = str(n)
    if '666' in st_n:
        li[i] = st_n
        if num == i:
            break
        i += 1
        
print(li[num])