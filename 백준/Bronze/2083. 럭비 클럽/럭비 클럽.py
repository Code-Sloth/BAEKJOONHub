while 1:
    name,age,weight = input().split()
    if name == '#': break
    if int(age) > 17 or int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')