from collections import deque
n, m = map(int, input().split())
Q, maze = deque([[0, 0]]), [[*map(int, list(input()))] for _ in range(n)]
while Q:
    x, y = Q.popleft()
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < n and 0 <= new_y < m and maze[new_x][new_y] == 1): continue
        Q.append([new_x, new_y]); maze[new_x][new_y] = maze[x][y] + 1
print(maze[n-1][m-1])