import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = [list(map(int,input().rstrip())) for _ in range(n)]
square = min(n,m)

for sq in range(square,1,-1):
    for i in range(n-sq+1):
        for j in range(m-sq+1):
            if g[i][j] == g[i][j+sq-1] == g[i+sq-1][j] == g[i+sq-1][j+sq-1]:
                print(sq**2)
                sys.exit()
else:
    print(1)