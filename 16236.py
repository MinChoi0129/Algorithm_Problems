from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

class BabyShark:
    def __init__(self, position):
        self.size = 2
        self.timer = 0
        self.position = position
        self.eatCount = 0
        
    def move(self, to, time):
        global board
        self.timer += time
        board[self.position[0]][self.position[1]] = 0 # 이동 전 위치 물고기 먹음
        self.position = to # 이동 완료
        self.eatCount += 1
        if self.eatCount == self.size:
            self.size += 1
            self.eatCount = 0
        board[to[0]][to[1]] = 0 # 이동 후 위치 물고기 먹음
    
    def bfs(self):
        global board, n 
        dxy = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
        q = deque([[self.position[0], self.position[1]]])
        visited = [[0] * n for _ in range(n)]
        visited[self.position[0]][self.position[1]] = 1
        approachableFishes = []

        while q:
            x, y = q.popleft()
            for dx, dy in dxy:
                newX, newY = x + dx, y + dy
                
                if newX < 0 or newX >= n or newY < 0 or newY >= n:
                    continue
                if visited[newX][newY] > 0 or board[newX][newY] > self.size:
                    continue
                
                visited[newX][newY] = visited[x][y] + 1
                
                if board[newX][newY] != 0 and board[newX][newY] < self.size:
                    approachableFishes.append([newX, newY])
                    
                q.append([newX, newY])

        closestDistance = 1e9
        closestFishes = []
        for fishPos in approachableFishes:
            if visited[fishPos[0]][fishPos[1]] <= closestDistance:
                closestDistance = visited[fishPos[0]][fishPos[1]]
                closestFishes.append(fishPos)
        
        closestFishes.sort(key = lambda x : (x[0], x[1]))
            
        return [closestFishes[0], closestDistance - 1] if closestFishes else -1
    
'''초기화'''
startPostition = [-1, -1]
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            startPostition = [i, j]

shark = BabyShark(startPostition)

'''동작'''
while True:
    fishes = shark.bfs()
    if fishes == -1:
        print(shark.timer)
        break
    else:
        shark.move(fishes[0], fishes[1])