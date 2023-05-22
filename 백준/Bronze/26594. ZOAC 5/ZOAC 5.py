S = input()
res = 1
for i in range(len(S)-1) :
    if S[i] == S[i+1] :
        res += 1
    else :
        break
print(res)