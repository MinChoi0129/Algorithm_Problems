from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

class BabyShark:
    def __init__(self, position):
        self.size = 2
        self.timer = 0
        self.position = position
        
    def move(self, to, time):
        board[self.position[0]][self.position[1]] = 0
        self.position = to
        self.timer += time
        self.size += board[to[0]][to[1]]
        board[to[0]][to[1]] = 0
    
    def getClosestFish(self):
        global board, n
        edibleFishes = []
        for i in range(n):
            for j in range(n):
                if board[i][j] in [1, 2, 3, 4, 5, 6] and board[i][j] < self.size:
                    edibleFishes.append([i, j])
        
        minDistance = 1e9
        closestFishes = []
        for fishPos in edibleFishes:
            d = self.나와물고기사이의astar거리(fishPos)
            if minDistance > d:
                closestFishes.clear()
                minDistance = d
                closestFishes.append(fishPos)
            else:
                closestFishes.append(fishPos)
            
        closestFishes.sort(key = lambda x : (x[0], x[1]))
        return [closestFishes[0], minDistance]
    
    def 나와물고기사이의astar거리(self, fishPos):
        global board, n
        start = self.position
        goal = fishPos
        
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        minf = 1e9
        effX, effY = -1, -1
        for xy in dxy:
            newX, newY = start[0] + xy[0], start[1] + xy[1]
            if not (0 <= newX < n and 0 <= newY < n):
                continue
            
            g = abs(newX - start[0]) + abs(newY - start[1])
            h = abs(newX - goal[0]) + abs(newY - goal[1])
            f = g + h
            if minf > f:
                minf, effX, effY = f, newX, newY
                

        return
    
    


'''초기화'''
startPostition = [-1, -1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            startPostition = [i, j]

shark = BabyShark(startPostition)


'''동작'''
while True:
    fishes = shark.getClosestFish()
    if fishes == -1:
        print(shark.timer)
        break
    else:
        shark.move(fishes[0], fishes[1])
