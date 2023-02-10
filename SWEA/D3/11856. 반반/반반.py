for t in range(1,int(input())+1):
    s = sorted(input().rstrip())
    print(f'#{t} Yes') if s[0] == s[1] and s[1] != s[2] and s[2] == s[3] else print(f'#{t} No')