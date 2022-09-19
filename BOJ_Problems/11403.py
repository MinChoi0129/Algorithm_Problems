def findRoute(x, y, visited):
    if visited[y] and x == y: return True
    
    for node in connections[x]:
        if not visited[node]:
            visited[node] = True
            result = findRoute(node, y, visited)
            if result: return 1
    
    return 0

n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
connections = {i: [] for i in range(n)}
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            connections[x].append(y)

answers = [[0] * n for _ in range(n)]
for x in range(n):
    for y in range(n):
        answers[x][y] = findRoute(x, y, [False] * n)
        
for line in answers: print(*line)