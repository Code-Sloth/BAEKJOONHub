import sys
input = sys.stdin.readline


li = '[]()'

while 1:
    s = input()
    if s[0] == '.':break
    st_s = ''
    for i in s:
        if i in li:
            st_s += i
    while '[]' in st_s or '()' in st_s:
        st_s = st_s.replace('[]','')
        st_s = st_s.replace('()','')

    print('no') if st_s else print('yes')