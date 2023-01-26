import sys
input = sys.stdin.readline

angle = [0] * 3
for _ in range(3):
    angle[_] = int(input())

if sum(angle) == 180:
    for i in angle:
        if angle.count(i) == 3:
            print('Equilateral')
            break
        if angle.count(i) == 2:
            print('Isosceles')
            break
    else: print('Scalene')
else:
    print('Error')