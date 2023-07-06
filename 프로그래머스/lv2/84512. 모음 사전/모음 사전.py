cnt = 0
answer = ''
def dfs(q,word):
    global cnt, answer
    if q == word:
        answer = cnt
        return
    
    if len(q) == 5: return

    li = ['A','E','I','O','U']
    for i in range(5):
        cnt += 1
        q.append(li[i])
        dfs(q,word)
        q.pop()
    
    return

def solution(word):
    word = list(word)
    q = []
    dfs(q,word)

    return answer