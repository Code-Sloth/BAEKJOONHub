a=int(input())
n=0
c=a

while True:    
    b = c//10 + c%10 # 2 + 6
    c = (c%10)*10 + b%10 # 6 8
    n += 1
    if c==a:
        break

print(n)