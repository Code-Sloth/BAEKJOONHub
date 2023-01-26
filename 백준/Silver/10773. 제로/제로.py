import sys
input = sys.stdin.readline

li = []
for _ in range(int(input())):
    n = int(input())
    li.append(n) if n!=0 else li.pop()
print(sum(li))