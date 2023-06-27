def dfs(node, visited):
    visited[node] = True
    for adj_node in connections[node]:
        if not visited[adj_node]:
            dfs(adj_node, visited)

n, m = map(int, input().split())
connections = {node : [] for node in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    connections[b].append(a)

max_value, answers = 0, []
for node in range(1, n+1):
    visited = {node: False for node in range(1, n+1)}
    dfs(node, visited)
    
    result = 0
    for computer in visited.values():
        if computer:
            result += 1
            
    if result > max_value:
        max_value = result
        answers = [node]
    elif result == max_value:
        answers.append(node)
        
print(*answers)