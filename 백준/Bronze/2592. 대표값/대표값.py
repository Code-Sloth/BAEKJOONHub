import sys
input = sys.stdin.readline

from collections import Counter

li = [int(input()) for _ in range(10)]
print(sum(li)//10,Counter(li).most_common(1)[0][0],sep='\n')