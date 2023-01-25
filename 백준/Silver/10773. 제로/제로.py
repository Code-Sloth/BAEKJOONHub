import sys
input = sys.stdin.readline

k = int(input())
st = []
for _ in range(k):
    n = int(input())
    st.pop() if n == 0 else st.append(n)
print(sum(st))