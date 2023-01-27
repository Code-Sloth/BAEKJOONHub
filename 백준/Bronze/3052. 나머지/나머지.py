import sys
input = sys.stdin.readline

se = set()
for i in range(10):
    se.add(int(input())%42)
print(len(se))