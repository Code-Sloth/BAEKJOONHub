answer = int(1e9)
a = [[1,1,1], [5,1,1], [25,5,1]]
mineral = {
    'diamond': 0,
    'iron': 1,
    'stone': 2
}

def dfs(index, p, minerals, d, ir, s):
    if index >= len(minerals) or d + ir + s == 0:
        global answer
        answer = min(answer, p)
        return 

    dp, ip, sp = 0, 0, 0
    for i in range(index, min(index+5, len(minerals))):
        dp += a[0][mineral[minerals[i]]]
        ip += a[1][mineral[minerals[i]]]
        sp += a[2][mineral[minerals[i]]]
 
    if d:
        dfs(index+5, p+dp, minerals, d-1, ir, s)
 
    if ir:
        dfs(index+5, p+ip, minerals, d, ir-1, s)
 
    if sp:
        dfs(index+5, p+sp, minerals, d, ir, s-1)
 
 
def solution(picks, minerals):
    global answer
    dfs(0, 0, minerals, picks[0], picks[1], picks[2])
    return answer