from collections import deque

def bfs(start_x, start_y, break_count):
    Q = deque([[break_count, start_x, start_y]])
    visited[break_count][start_x][start_y] = 1
    
    while Q:
        break_count, x, y = Q.popleft()
        if (x, y) == (n-1, m-1):
            return visited[break_count][x][y]
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m: # 범위 내
                if board[new_x][new_y] == 1: # 벽이 있음
                    if break_count < k and visited[break_count + 1][new_x][new_y] == -1:
                        visited[break_count + 1][new_x][new_y] = visited[break_count][x][y] + 1
                        Q.append([break_count + 1, new_x, new_y])
                else: # 벽이 없고 그냥 길임
                    if visited[break_count][new_x][new_y] == -1:
                        visited[break_count][new_x][new_y] = visited[break_count][x][y] + 1
                        Q.append([break_count, new_x, new_y])
    return -1

n, m, k = map(int, input().split())
board = [[*map(int, list(input()))] for _ in range(n)]
visited = [[[-1] * m for _ in range(n)] for _ in range(k+1)]

print(bfs(start_x=0, start_y=0, break_count=0))