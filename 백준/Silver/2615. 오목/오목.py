import sys
input = sys.stdin.readline

g = [list(map(int,input().split())) for _ in range(19)]
d = [(-1,1),(1,0),(1,1),(0,1)]

for x in range(19):
    for y in range(19):
        if g[x][y]:
            a = g[x][y]
            for dx,dy in d:
                nx,ny = x+dx,y+dy
                t = 1

                for _ in range(4):
                    if 0 <= nx < 19 and 0 <= ny < 19 and g[nx][ny] == a:
                        t += 1
                    else: break

                    if t == 5:
                        if 0 <= nx+dx < 19 and 0 <= ny+dy < 19 and g[nx+dx][ny+dy] == a:
                            break
                        if 0 <= x-dx < 19 and 0 <= y-dy < 19 and g[x-dx][y-dy] == a:
                            break
                        print(a)
                        print(x+1,y+1)
                        sys.exit()
                    nx += dx
                    ny += dy
print(0)
