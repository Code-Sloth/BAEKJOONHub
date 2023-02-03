credit = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,int(input())+1):
    n, k = map(int,input().split())
    po = [0] * n
    for i in range(n):
        li = list(map(int,input().split()))
        po[i] = li[0] * 0.35 + li[1] * 0.45 + li[2] * 0.20
    me = po[k-1]
    po.sort(reverse=True)
    me_grade = po.index(me)
    print(f'#{t}',credit[me_grade//(n//10)])