d = 0
m = [31,28,31,30,31,30,31,31,30,31,30,31]
w = ['SUN','MON','TUE','WED','THU','FRI','SAT']

a, b = map(int,input().split())

for i in range(a-1):
    d += m[i]

d = (d+b) % 7

print(w[d])