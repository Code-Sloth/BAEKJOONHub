import string

s = input()
up = string.ascii_uppercase
low = string.ascii_lowercase
rot_up = up[13:] + up[:13]
rot_low = low[13:] + low[:13]

trans_up = str.maketrans(up,rot_up)
trans_low = str.maketrans(low,rot_low)

s = s.translate(trans_up)
s = s.translate(trans_low)

print(s)