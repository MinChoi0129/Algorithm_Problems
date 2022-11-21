import sys
from collections import deque

class Shark:
    def __init__(self, x, y, speed, direction, size):
        self.x, self.y = x, y
        self.speed = speed
        self.direction = direction
        self.size = size
        self.moved = False

    def move(self):
        required_move_times = self.speed

        if self.direction == 1:
            if required_move_times > self.x:
                required_move_times -= self.x
                direction_set = required_move_times // r # 몫
                leftover_set = (required_move_times % r) + 1 # 나머지

                if direction_set % 2 == 0:
                    self.direction = 2
                    self.x += leftover_set
                else:
                    self.x = r-1
                    self.x -= leftover_set
            else:
                self.x -= required_move_times
        
        elif self.direction == 2:
            if required_move_times > (r-1) - self.x:
                required_move_times -= (r-1) - self.x
                self.x = r-1
                direction_set = required_move_times // r
                leftover_set = ((required_move_times % r) + 1) % (r-1)

                if direction_set % 2 == 0:
                    self.direction = 1
                    self.x -= leftover_set
                else:
                    self.x = 0
                    self.x += leftover_set
            else:
                self.x += required_move_times

        elif self.direction == 3:
            if required_move_times > (c-1) - self.y:
                required_move_times -= (c-1) - self.y
                self.y = c-1
                direction_set = required_move_times // c
                leftover_set = ((required_move_times % c) + 1) % (c-1)

                if direction_set % 2 == 0:
                    self.direction = 4
                    self.y -= leftover_set
                else:
                    self.y = 0
                    self.y += leftover_set
            else:
                self.y += required_move_times
        
        elif self.direction == 4:
            if required_move_times > self.y:
                required_move_times -= self.y
                self.y = 0
                direction_set = required_move_times // c
                leftover_set = ((required_move_times % c) + 1) % (c-1)

                if direction_set % 2 == 0:
                    self.direction = 3
                    self.y += leftover_set
                else:
                    self.y = c-1
                    self.y -= leftover_set
            else:
                self.y -= required_move_times

        self.moved = True
        fishing_ground[self.x][self.y].append(self)

class Human:
    def __init__(self): self.bucket = 0; self.col = -1
    def move(self): self.col += 1
    def catchCloestShark(self, r):
        for x in range(r):
            if fishing_ground[x][self.col]:
                self.bucket += fishing_ground[x][self.col][0].size
                fishing_ground[x][self.col] = deque()
                break

def initializer():
    input = lambda : sys.stdin.readline().rstrip()
    r, c, m = map(int, input().split())
    fishing_ground = [[deque() for y in range(c)] for x in range(r)]
    for _ in range(m):
        big_x, big_y, speed, direction, size = map(int, input().split())
        fishing_ground[big_x-1][big_y-1] = deque([Shark(big_x-1, big_y-1, speed, direction, size)])
    return r, c, m, fishing_ground

r, c, m, fishing_ground = initializer()
fisher = Human()

for _ in range(c):
    fisher.move()
    fisher.catchCloestShark(r)
    for x in range(r):
        for y in range(c):
            element = fishing_ground[x][y]
            if element and not element[0].moved:
                shark = element.popleft()
                shark.move()

    for x in range(r):
        for y in range(c):
            if fishing_ground[x][y]:
                fishing_ground[x][y][0].moved = False
            if len(fishing_ground[x][y]) >= 2:
                largest_shark_idx, largest_shark_size = None, 0
                for idx, shark in enumerate(fishing_ground[x][y]):
                    if shark.size > largest_shark_size:
                        largest_shark_idx, largest_shark_size = idx, shark.size
                fishing_ground[x][y] = deque([fishing_ground[x][y][largest_shark_idx]])

print(fisher.bucket)

