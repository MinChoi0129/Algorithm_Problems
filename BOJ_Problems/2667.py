n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def DFS(x, y):
    global size
    
    if not (0 <= x < n and 0 <= y < n) or visited[x][y] or board[x][y] == '0':
        return False

    if board[x][y] == '1':
        visited[x][y] = True
        size += 1
        for dx, dy in dxy:
            DFS(x + dx, y + dy)
        return True
 
results = []
size = 0
for x in range(n):
    for y in range(n):
        if DFS(x, y):
            results.append(size)
            size = 0

results.sort()
print(len(results))
for s in results:
    print(s)