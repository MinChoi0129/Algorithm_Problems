import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs():
    n, m = map(int, input().split())
    board = [[*map(int, list(input()))] for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    
    Q = deque() # 큐 초기화
    Q.append([0, 0, 0])
    visited[0][0][0] = 1
    while Q:
        x, y, mode = Q.popleft()
        
        if x == n - 1 and y == m - 1: # 도착했다면
            return visited[x][y][mode]
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
            newX, newY = x + dx, y + dy
            
            if 0 <= newX < n and 0 <= newY < m: # 범위 내
                if board[newX][newY] == 1 and mode == 0: # 벽이 있는데 뚫은적 없는 경우
                    visited[newX][newY][1] = visited[x][y][0] + 1 # 벽을 뚫어봄.
                    Q.append([newX, newY, 1])
                elif board[newX][newY] == 0 and visited[newX][newY][mode] == 0: # 벽이 없고 가본적도 없고
                    visited[newX][newY][mode] = visited[x][y][mode] + 1
                    Q.append([newX, newY, mode])
                    
                
    return -1 # 가볼 수 있는데는 다 가봤지만 Q가 비었고 목적지 도달 못한 경우

print(bfs())