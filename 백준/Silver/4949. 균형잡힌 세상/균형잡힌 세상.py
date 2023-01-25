import sys
input = sys.stdin.readline


li = '[]()'

while 1:
    s = input()
    if s[0] == '.':break
    st_s = ''
    for i in s:
        if i in li:
            st_s += s[s.index(i)]
    while 1:
        st_s = st_s.replace('[]','')
        st_s = st_s.replace('()','')
        if '[]' not in st_s and '()' not in st_s:break
    if st_s:print('no')
    else:print('yes')