import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mon = int(input())
    q = mon // 25
    d = (mon % 25) // 10
    n = (mon % 25) % 10 // 5
    p = (mon % 25 ) % 10 % 5
    print(q, d, n, p, sep = ' ')