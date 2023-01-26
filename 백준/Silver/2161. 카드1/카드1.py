import sys

input = sys.stdin.readline

from collections import deque
st = deque()
for i in range(1,int(input())+1):
    st.append(i)

li = []
while 1:
    print(st.popleft(),end = ' ')
    if st:
        st.append(st.popleft())
    else:break