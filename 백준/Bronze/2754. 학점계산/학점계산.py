po = list(input())

di = {'A':4, 'B':3, 'C':2, 'D':1, '+':+0.3, '0':+0.0, '-':-0.3}
if po == ['F']: print(0.0)
else:print(di[po[0]]+di[po[1]])