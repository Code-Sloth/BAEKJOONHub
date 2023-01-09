n = int(input())

t = 0
num = 1
if n == 1:
    num =1
else:
    while True:
        t += 1
        tt = 3*t**2-3*t+2
        if n in range(tt,3*(t+1)**2-3*(t+1)+2):
            num = t+1
            break
print(num)