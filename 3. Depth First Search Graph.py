V = int(input())
E = int(input())
adj = [[] for i in range(V)]
for i in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
start_node = int(input())

visited = [False] * V
result = []

def dfs(node):
    visited[node] = True
    result.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(start_node)
print(*(result))