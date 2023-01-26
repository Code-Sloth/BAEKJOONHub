import sys
input = sys.stdin.readline

li = list(range(1, int(input())+1))
while 1:
    try:
        print(li[0],end=' ')
        del li[0]
        li.append(li[0])
        del li[0]
    except:break