import sys
input = sys.stdin.readline

st = []
pl = []

c = 1
is_ = 1
for _ in range(int(input())):
    n = int(input())
    while c <= n:
        st.append(c)
        pl.append('+')
        c += 1
    if st[-1] == n:
        st.pop()
        pl.append('-')
    else:
        is_ = 0
        print('NO')
        break
if is_:
    print('\n'.join(pl))