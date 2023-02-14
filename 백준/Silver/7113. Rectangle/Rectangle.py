import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

x, y = map(int,input().split())
t = 0

def square(mx,mn):
    global t
    if mx == 0 or mn == 0: return
    if mx == mn:
        t += 1
        return
    t += mx//mn
    mx %= mn
    square(mn,mx)
    
square(max(x,y),min(x,y))
print(t)