n, m = map(int, input().split())

board = []
answer = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
start_point = (-1, -1)
for x in range(n):
    line = [*map(int, input().split())]
    for y in range(m):
        if line[y] == 2:
            start_point = (x, y)
    board.append(line)


def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if not visited[new_x][new_y] and board[new_x][new_y] != 0:
            answer[new_x][new_y] = answer[x][y] + 1
            dfs(new_x, new_y)
