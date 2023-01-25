import sys
input = sys.stdin.readline

t = int(input())
st = [0] * t
st2 = []
pl = []
li = []

for i in range(t):
    st[i] = int(input())

for i in range(1,t+1):
    li.append(i)
    pl.append('+')
    while li and li[-1] == st[0]:
        st2.append(li.pop())
        st.pop(0)
        pl.append('-')
if li:print('NO')
else:print(*pl,sep='\n')