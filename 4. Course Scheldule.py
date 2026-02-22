N = int(input())
M = int(input())
adj = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    adj[v].append(u)
visited = [False] * N
path = [False] * N

def has_cycle(u):
    visited[u] = True
    path[u] = True
    
    for neighbor in adj[u]:
        if path[neighbor]:
            return True
        if not visited[neighbor]:
            if has_cycle(neighbor):
                return True
                
    path[u] = False
    return False
possible = 1
for i in range(N):
    if not visited[i]:
        if has_cycle(i):
            possible = 0
            break
print(possible)