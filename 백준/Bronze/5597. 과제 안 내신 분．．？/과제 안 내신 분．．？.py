import sys

a=list(range(1,31))

for i in range(28):
    b=int(sys.stdin.readline())
    a.remove(b)

print(min(a),max(a),sep='\n')