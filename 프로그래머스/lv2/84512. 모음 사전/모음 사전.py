from itertools import product

def solution(word):
    g = []
    
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            pro = ''.join(list(c))
            g.append(pro)

    g.sort()
    return g.index(word) + 1