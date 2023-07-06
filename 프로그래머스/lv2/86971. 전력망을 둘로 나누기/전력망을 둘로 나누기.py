from collections import deque

def bfs(x,g,vi):
    q = deque([x])
    vi[x] = 1
    cnt = 1

    while q:
        now = q.popleft()
        
        for i in g[now]:
            if not vi[i]:
                vi[i] = 1
                cnt += 1
                q.append(i)
                
    return cnt
        
def solution(n, wires):
    answer = n
    g = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        g[v1].append(v2)
        g[v2].append(v1)
            
    for a,b in wires:
        vi = [0] * (n+1)
        vi[b] = 1
        cnt = bfs(a,g,vi)
        answer = min(answer, abs(cnt - (n-cnt)))
        
    return answer