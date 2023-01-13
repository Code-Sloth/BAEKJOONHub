import math
a,b,v = map(int,input().split())

end = v - a
sep = a - b
share = end / sep
print(math.ceil(share)+1)