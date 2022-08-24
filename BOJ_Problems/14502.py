from copy import deepcopy as DC
from collections import deque

def buildWall(board, count):
    global maximum_safety
    
    if count == 3:
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_board = DC(board)
        virus_locations = deque([])
        for x in range(n):
            for y in range(m):
                if new_board[x][y] == 2:
                    virus_locations.append([x, y])
                    
        while virus_locations:
            virusX, virusY = virus_locations.popleft()
            for dx, dy in dxy:
                newX, newY = virusX + dx, virusY + dy
                if 0 <= newX < n and 0 <= newY < m:
                    if new_board[newX][newY] == 0:
                        new_board[newX][newY] = 2
                        virus_locations.append([newX, newY])

        safety = 0
        for line in new_board:
            for num in line:
                if num == 0:
                    safety += 1
        
        maximum_safety = max(maximum_safety, safety)

    else:
        for x in range(n):
            for y in range(m):
                if board[x][y] == 0: # 벽이 아니면
                    board[x][y] = 1 # 벽을 잠시 세움
                    buildWall(board, count + 1)
                    board[x][y] = 0 # 원상복구
  
  
n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]

      
maximum_safety = 0     
buildWall(board, 0)
print(maximum_safety)