import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
board = [[0] * n for _ in range(n)]
commands, times = [], []

for _ in range(int(input())):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

for _ in range(int(input())):
    clock, direction = input().split()
    commands.append([int(clock), direction])
    
for cmd in commands:
    times.append(cmd[0])

class SnakeError(Exception):
    pass
   
class Snake:
    
    def __init__(self, heading):
        self.heading = heading
        self.bodyElements = deque([[0, 0]])
        self.head = self.bodyElements[0]
        self.timer = 0
        
    def turnTo(self, direction):
        if self.heading == "East":
            if direction == "D":
                self.heading = "South"
            else:
                self.heading = "North"
                
        elif self.heading == "West":
            if direction == "D":
                self.heading = "North"
            else:
                self.heading = "South"
                
        elif self.heading == "South":
            if direction == "D":
                self.heading = "West"
            else:
                self.heading = "East"
                
        elif self.heading == "North":
            if direction == "D":
                self.heading = "East"
            else:
                self.heading = "West"
    
    def canMove(self):
        if self.heading == 'East':
            if self.head[1] + 1 == n or [self.head[0], self.head[1] + 1] in self.bodyElements:
                return False
            return True
        elif self.heading == 'West':
            if self.head[1] - 1 == -1 or [self.head[0], self.head[1] - 1] in self.bodyElements:
                return False
            return True
        elif self.heading == 'South':
            if self.head[0] + 1 == n or [self.head[0] + 1, self.head[1]] in self.bodyElements:
                return False
            return True
        elif self.heading == 'North':
            if self.head[0] - 1 == -1 or [self.head[0] - 1, self.head[1]] in self.bodyElements:
                return False
            return True
        
    def move(self):
        self.timer += 1
        
        if self.heading == 'East':
            newX, newY = self.head[0], self.head[1] + 1
        elif self.heading == "West":
            newX, newY = self.head[0], self.head[1] - 1
        elif self.heading == "South":
            newX, newY = self.head[0] + 1, self.head[1]
        elif self.heading == "North":
            newX, newY = self.head[0] - 1, self.head[1]
        
        if self.canMove():
            if board[newX][newY] == 1:
                self.bodyElements.appendleft([newX, newY])
                board[newX][newY] = 0
                self.head = self.bodyElements[0]
            else:
                self.bodyElements.appendleft([newX, newY])
                self.bodyElements.pop()
                self.head = self.bodyElements[0]
        else:
            raise SnakeError
            
snake = Snake("East")

while True:
    try:
        snake.move()
        if snake.timer in times:
            snake.turnTo(commands[times.index(snake.timer)][1])
    except:
        print(snake.timer)
        break