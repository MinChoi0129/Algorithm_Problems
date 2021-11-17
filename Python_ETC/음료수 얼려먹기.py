def dfs(x, y):
    global graph, height, width, dx, dy, count
    
    if (x <= -1 or x >= height or y <= -1 or y >= width) or graph[x][y] == 1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        
        return True

height, width = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

for i in range(height):
    graph.append(list(map(int, input())))

for x in range(height):
    for y in range(width):
        if dfs(x, y):
            count += 1
        
print(count)