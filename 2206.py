import sys
from collections import deque

n, m = map(int, input().split())
board = [[*map(int, list(input()))] for _ in range(n)]
visited = [[0] * m for _ in range(n)]

def bfs(board, start, visited):
    
    Q = deque([start]) # 큐 초기화
    visited[start[0]][start[1]] = 1
    while Q:
        x, y, breakCounter = Q.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
            newX, newY = x + dx, y + dy
            if newX < 0 or newX >= n or newY < 0 or newY >= m:
                continue
            if visited[newX][newY] > 0:
                continue
            
            visited[newX][newY] = visited[x][y] + 1

            if board[newX][newY] == 1:
                if breakCounter == 1:
                    continue
                else:
                    board[newX][newY] = 0
                    Q.append([newX, newY, 1])
            else:
                if breakCounter == 1:
                    Q.append([newX, newY, 1])
                else:
                    Q.append([newX, newY, 0])
                
   
bfs(board, [0, 0, 0], visited)

print(-1 if visited[n-1][m-1] == 0 else visited[n-1][m-1])