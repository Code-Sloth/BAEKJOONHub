for i in range(int(input())):
    li_s = []
    li_al = []
    for _ in range(int(input())):
        s,al = input().split()
        li_s.append(s)
        li_al.append(int(al))
    print(li_s[li_al.index(max(li_al))])