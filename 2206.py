import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

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
            if newX == n-1 and newY == m-1:
                return visited[newX][newY]
            
            
            
            if board[newX][newY] == 1:
                if breakCounter == 1:
                    continue
                else:
                    Q.append([newX, newY, 1])
            else:
                Q.append([newX, newY, breakCounter])
    return -1

print(bfs(board, [0, 0, 0], visited))