def dfs(node_num):
    if not visited[node_num]:
        visited[node_num] = True
        for node in connections[node_num]:
            dfs(node)
        order.append(node_num)

n, m = map(int, input().split())
connections = {i: [] for i in range(1, n+1)}

visited = [None] + [False] * n
order = []

for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)

for i in range(1, n+1):
    dfs(i)

print(*reversed(order))