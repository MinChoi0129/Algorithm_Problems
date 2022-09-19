def doesRouteExist(x, y, visited):
    if visited[y] and x == y: return 1
    for node in connections[x]:
        if not visited[node]:
            visited[node] = True
            result = doesRouteExist(node, y, visited)
            if result: return 1
    return 0

n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
answer = [[0]*n for _ in range(n)]
connections = {i:[] for i in range(n)}

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1: connections[x].append(y)

for x in range(n):
    for y in range(n): answer[x][y] = doesRouteExist(x, y, [False] * n)

for line in answer: print(*line)