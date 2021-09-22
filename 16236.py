from collections import deque
from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

class BabyShark:
    def __init__(self, position):
        self.size = 2
        self.timer = 0
        self.position = position
        
    def move(self, to, time):
        global board
        board[self.position[0]][self.position[1]] = 0
        self.position = to
        self.timer += time
        self.size += board[to[0]][to[1]]
        board[to[0]][to[1]] = 0
    
    def getClosestFish(self): # 여러좌표를 리턴할 수도, -1을 리턴할수도 있음
        global board, n
        edibleFishes = [] # 보이는 먹을 수 있는 물고기 그냥 다 담음
        for i in range(n):
            for j in range(n):
                if board[i][j] in [1, 2, 3, 4, 5, 6] and board[i][j] < self.size:
                    edibleFishes.append([i, j])
        
        
        
        
        minDistance = 1e9
        closestFishes = []
        for fishPos in edibleFishes: # 보이는 물고기들 중에서
            d = self.나와물고기사이의astar거리(fishPos) # 어느 한마리 붙잡고 거리측정
            if minDistance > d:
                closestFishes.clear()
                minDistance = d
                closestFishes.append(fishPos)
            elif minDistance == d:
                closestFishes.append(fishPos)
            else:
                continue
        
        #결국 closestFishes에는 최단거리 1마리 이상의 좌표가 담김
            
            
        closestFishes.sort(key = lambda x : (x[0], x[1]))
        return [closestFishes[0], minDistance]
    
    def 나와물고기사이의astar거리(self, fishPos):
        global board, n
        start = deepcopy(self.position)
        goal = fishPos
        distanceCalculator = 0
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        #goal이 아예 inapprochable한지
        
        apprachable = False
        for xy in dxy:
            newX, newY = goal[0] + xy[0], goal[1] + xy[1]
            if not (0 <= newX < n and 0 <= newY < n):
                continue
            
            # 여기는 보드 안
            newPoint = board[newX][newY]
            if newPoint <= self.size:
                apprachable = True
                break
            
        if not apprachable:
            return -1
        
        visited = [[False]*n for _ in range(n)]
        visited[self.position[0]][self.position[1]] = True
        
        while True:
            if start == goal:
                return distanceCalculator
            
            effF = 1e9
            effX, effY = -1, -1
            for xy in dxy:
                newX, newY = start[0] + xy[0], start[1] + xy[1]
                
                if not (0 <= newX < n and 0 <= newY < n):
                    continue
                
                if board[newX][newY] > self.size and board[newX][newY] != 9:
                    continue
                
                if visited[newX][newY]:
                    continue
                visited[newX][newY] = True
                g = abs(newX - self.position[0]) + abs(newY - self.position[1])
                h = abs(newX - goal[0]) + abs(newY - goal[1])
                f = g + h
                if effF > f:
                    effF, effX, effY = f, newX, newY
            start[0], start[1] = effX, effY
            distanceCalculator += 1
    

'''초기화'''
startPostition = [-1, -1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            startPostition = [i, j]

shark = BabyShark(startPostition)


'''동작'''
while True:
    fishes = shark.getClosestFish() # 여러개 들어올 수도 있음
    if fishes == -1:
        print(shark.timer)
        break
    else:
        shark.move(fishes[0], fishes[1])
