import sys
from collections import deque

class Shark:
    def __init__(self, x, y, speed, direction, size):
        self.x, self.y = x, y
        self.speed = speed
        self.direction = direction
        self.size = size
        self.moved = False
    
    def isFrontWall(self):
        if self.direction == 1:
            return self.x == 0
        elif self.direction == 2:
            return self.x == r-1
        elif self.direction == 3:
            return self.y == c-1
        elif self.direction == 4:
            return self.y == 0

    def move(self):
        for _ in range(self.speed):
            if self.direction == 1:
                if self.isFrontWall(): self.direction = 2; self.x += 1
                else: self.x -= 1
            elif self.direction == 2:
                if self.isFrontWall(): self.direction = 1; self.x -= 1
                else: self.x += 1
            elif self.direction == 3:
                if self.isFrontWall(): self.direction = 4; self.y -= 1
                else: self.y += 1
            elif self.direction == 4:
                if self.isFrontWall(): self.direction = 3; self.y += 1
                else: self.y -= 1
        
        new_shark = Shark(self.x, self.y, self.speed, self.direction, self.size)
        new_shark.moved = True
        fishing_ground[self.x][self.y].append(new_shark)

class Human:
    def __init__(self):
        self.bucket = 0
        self.col = -1
    def move(self):
        self.col += 1
    def catchCloestShark(self, r):
        for x in range(r):
            if fishing_ground[x][self.col]:
                self.bucket += fishing_ground[x][self.col][0].size
                fishing_ground[x][self.col] = deque()
                break

input = lambda : sys.stdin.readline().rstrip()
r, c, m = map(int, input().split())
fishing_ground = [[deque()] * c for _ in range(r)]
for _ in range(m):
    big_x, big_y, speed, direction, size = map(int, input().split())
    fishing_ground[big_x-1][big_y-1] = deque([Shark(big_x-1, big_y-1, speed, direction, size)])

fisher = Human()

for _ in range(c):
    fisher.move()
    fisher.catchCloestShark(r)
    for x in range(r):
        for y in range(c):
            try:
                element = fishing_ground[x][y][0]
                if not element.moved:
                    element.move()
            except: continue
    
    for x in range(r):
        for y in range(c):
            if fishing_ground[x][y]:
                largest_shark_idx, largest_shark_size = None, 0
                for idx, shark in enumerate(fishing_ground[x][y]):
                    if shark.size > largest_shark_size:
                        largest_shark_idx, largest_shark_size = idx, shark.size
                fishing_ground[x][y] = [fishing_ground[x][y][largest_shark_idx]]

print(fisher.bucket)