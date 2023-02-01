from sys import stdin

n = int(stdin.readline())
v = int(stdin.readline())

graph = [ [] for _ in range(n+1) ]
visited = [0] * (n+1)

for i in range(v) : 
    a, b = map(int, stdin.readline().split())

    graph[a] += [b]
    graph[b] += [a]

def dfs(k) : 
    visited[k] = 1

    for nx in graph[k] : 
        if visited[nx] == 0 : 
            dfs(nx)

dfs(1)
print(sum(visited)-1)