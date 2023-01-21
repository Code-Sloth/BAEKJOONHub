distance = []
x,y,w,h = map(int,input().split())
if x >= w/2:
    distance.append(w - x)
else:
    distance.append(x)
if y >= h/2:
    distance.append(h - y)
else:
    distance.append(y)
print(min(distance))