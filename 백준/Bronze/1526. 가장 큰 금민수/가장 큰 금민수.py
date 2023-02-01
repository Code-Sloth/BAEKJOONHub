import sys
input = sys.stdin.readline

n = int(input())
set_74 = [{'4'},{'7'},{'4','7'},{'7','4'}]

for i in range(n,3,-1):
    if set(str(i)) in set_74:
        print(i)
        break