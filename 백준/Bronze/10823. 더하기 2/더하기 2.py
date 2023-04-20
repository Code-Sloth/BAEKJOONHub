n = ''
while 1:
    try:
        n += input()
    except:
        break
print(sum(map(int, n.split(','))))