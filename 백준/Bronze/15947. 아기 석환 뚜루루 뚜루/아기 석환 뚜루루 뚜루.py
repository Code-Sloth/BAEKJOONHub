import sys
input = sys.stdin.readline

g = ['.', 'baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']

n = int(input())
n_re = n % 14
n_sh = n // 14

if not n_re: n_re = 14

if 'turu' in g[n_re]:
    result = g[n_re] + 'ru'*n_sh
    if 'rururururu' in result:
        print(f"tu+ru*{result.count('r')}")
    else:
        print(result)
else:
    print(g[n_re])