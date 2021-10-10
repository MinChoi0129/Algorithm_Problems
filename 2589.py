from copy import deepcopy as DC
from collections import deque

height, width = map(int, input().split())
treasure_map = [list(input()) for _ in range(height)]

starts = []
for x in range(height):
    for y in range(width):
        if treasure_map[x][y] == 'L':
            starts.append([x, y])

def bfs(board, startX, startY):
    
    Q = deque([[startX, startY]])
    visited = [[0] * width for _ in range(height)]
    visited[startX][startY] += 1
    
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    lastX, lastY = -1, -1
    while Q:
        x, y =  Q.popleft()
        lastX, lastY = x, y
        for dx, dy in dxy:
            newX, newY = x + dx, y + dy
            if not (0 <= newX < height and 0 <= newY < width): # Out_Of_Index
                continue
            if board[newX][newY] == 'W': # 바다인 경우
                continue
            if visited[newX][newY] > 0: # 방문했던 경우
                continue
            
            visited[newX][newY] = visited[x][y] + 1
            Q.append([newX, newY])
    
    return visited[lastX][lastY] - 1

bfs_longest = -1
for start in starts:
    copied_treasure_map = DC(treasure_map)
    result = bfs(copied_treasure_map, start[0], start[1])
    bfs_longest = max(bfs_longest, result)
print(bfs_longest)