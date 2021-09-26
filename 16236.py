import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

class BabyShark:
    def __init__(self, position):
        self.size = 2 # 몸집
        self.timer = 0 # 걸린 시간
        self.eatCount = 0 # 먹은 횟수
        self.position = position # 현위치 [x, y]
        
    def move(self, to, time):
        global board
        
        self.timer += time # 현위치에서 to까지 가는데 걸리는 시간
        
        board[self.position[0]][self.position[1]] = 0 # 이동 전 위치 물고기 먹음
        self.position = to # 이동
        board[to[0]][to[1]] = 0 # 이동 후 위치 물고기 먹음
        
        self.eatCount += 1 # 1회먹음
        if self.eatCount == self.size: # 크기만큼 먹어야 몸집 1 증가
            self.size += 1
            self.eatCount = 0 # 몸 커졌으니 다시 먹은 횟수 초기화
            
 
    def bfs(self):
        global board, n 
        
        Q = deque([[self.position[0], self.position[1]]]) # 큐 초기화
        visited = [[0] * n for _ in range(n)] # 방문횟수 초기화
        visited[self.position[0]][self.position[1]] = 1 # 첫 위치 방문처리
        

        approachableFishes = [] # 닿을 수 있으면서 먹을수도 있는 물고기들
        while Q:
            x, y = Q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
                newX, newY = x + dx, y + dy # 상하좌우 중 어느 한 위치
                
                if newX < 0 or newX >= n or newY < 0 or newY >= n:
                    # 보드 벗어남
                    continue
                if visited[newX][newY] > 0 or board[newX][newY] > self.size:
                    # 방문했거나(안지나갈 것임)
                    # 자기보다 더 큰 물고기가 있거나(못지나감)
                    continue
                
                visited[newX][newY] = visited[x][y] + 1
                # 위 두 조건 모두 아닌 경우 갈 수 있으며, 이곳까지의 거리는 기존위치에서 +1 한 거리
                
                
                if board[newX][newY] != 0 and board[newX][newY] < self.size: # 먹을 수 있음
                    approachableFishes.append([newX, newY])
                    
                Q.append([newX, newY]) # 39번줄에서 얘기한 어느 한 위치에서 새롭게 또 상하좌우 탐색할 예정

        closestDistance = 1e9 # 최단거리(유일)
        closestFishes = [] # 최단거리의 물고기들(복수 가능)
        for fishPos in approachableFishes:
            if visited[fishPos[0]][fishPos[1]] <= closestDistance: # =(등호) 있어야 복수 가능 *중요*
                closestDistance = visited[fishPos[0]][fishPos[1]]
                closestFishes.append(fishPos)
        
        closestFishes.sort(key = lambda x : (x[0], x[1]))
            
        return [closestFishes[0], closestDistance - 1] if closestFishes else -1
                                # 1을 빼는 이유는 실제 위에서 visited처리할 때 최단거리보다 1크게 했기때문.
                                # 왜 1을 크게 했냐면 초기위치(9) 에서 1로 안 만들면 미방문처리가 되기때문에 1부터 출발한 것임.

'''Initializing'''
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

startPostition = [-1, -1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            startPostition = [i, j]
shark = BabyShark(startPostition)

'''Activation'''
while True:
    fishes = shark.bfs()
    if fishes == -1:
        print(shark.timer)
        break
    else:
        location, distance = fishes
        shark.move(location, distance)