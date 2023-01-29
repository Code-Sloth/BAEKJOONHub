import sys
input = sys.stdin.readline

li = [int(input()) for x in range(5)]
print(sum(li)//len(li),sorted(li)[2],sep='\n')