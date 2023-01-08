import string

s = input()
li = []
abc = string.ascii_lowercase
s2 = s.lower()

for i in abc:
    li.append(s2.count(i)) # li에 i가 몇개있는지 리스트로 저장
    b = li.index(max(li)) # 최댓값 인덱스를 b에 저장

if max(li) not in li[b+1:]: # 최댓값이 li의 최댓값인덱스 다음부터 없으면
    print(abc[b].upper())
else:
    print('?')