from collections import deque

def isProperCoordinate(x, y): return 0 <= x < n and 0 <= y < m and not visited[x][y] and board[x][y] == 0
def search(x, y):
    Q = deque([(x, y)]); visited[x][y] = True
    size = 1
    while Q:
        x, y = Q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if isProperCoordinate(new_x, new_y):
                Q.append((new_x, new_y)); size += 1
                visited[new_x][new_y] = True
    return size

m, n, k = map(int, input().split())
board, visited, areas = [[0] * m for _ in range(n)], [[False] * m for _ in range(n)], []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1

for x in range(n):
    for y in range(m):
        if isProperCoordinate(x, y): areas.append(search(x, y))

areas.sort()
print(len(areas))
print(*areas)