from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

class Shark:
    def __init__(self, x, y, speed, direction, size):
        self.x, self.y = x, y
        self.speed = speed
        self.direction = direction
        self.size = size
        self.moved = False

    def move(self, fishing_ground, r, c):
        d = self.direction
        n, distance_to_move = r if d < 3 else c, self.speed
        opposite_direction, distance_to_facing_end = None, None
        if   d == 1: opposite_direction = 2; distance_to_facing_end = self.x
        elif d == 2: opposite_direction = 1; distance_to_facing_end = (n-1) - self.x
        elif d == 3: opposite_direction = 4; distance_to_facing_end = (n-1) - self.y
        elif d == 4: opposite_direction = 3; distance_to_facing_end = self.y
                    
        if d < 3:
            if distance_to_move <= distance_to_facing_end: self.x += distance_to_move * ((-1) ** d)
            else:
                distance_to_move -= distance_to_facing_end
                self.x = 0 if d == 1 else n-1
                if (distance_to_move // (n-1)) % 2 == 0:
                    self.x += (distance_to_move % (n-1)) * ((-1) ** (d - 1))
                    self.direction = opposite_direction
                else: self.x = (n-1) - self.x + (distance_to_move % (n-1)) * ((-1) ** d)
        
        else:
            if distance_to_move <= distance_to_facing_end: self.y += distance_to_move * ((-1) ** (d - 1))
            else:
                distance_to_move -= distance_to_facing_end
                self.y = n-1 if d == 3 else 0
                if (distance_to_move // (n-1)) % 2 == 0:
                    self.y += (distance_to_move % (n-1)) * ((-1) ** d)
                    self.direction = opposite_direction
                else: self.y = (n-1) - self.y + (distance_to_move % (n-1)) * ((-1) ** (d - 1))

        self.moved = True
        fishing_ground[self.x][self.y].append(self)
    
    @staticmethod
    def moveAllSharks(fishing_ground, r, c):
        for x in range(r):
            for y in range(c):
                element = fishing_ground[x][y]
                if element and not element[0].moved:
                    shark = element.popleft()
                    shark.move(fishing_ground, r, c)
    
    @staticmethod
    def setBiggestShark(fishing_ground, r, c):
        for x in range(r):
            for y in range(c):
                if fishing_ground[x][y]:
                    biggest_shark = max(fishing_ground[x][y], key=lambda obj: obj.size)
                    biggest_shark.moved = False
                    fishing_ground[x][y] = deque([biggest_shark])

class Human:
    def __init__(self): self.bucket = 0; self.col = -1
    def move(self): self.col += 1
    def catchCloestShark(self, fishing_ground, r, c):
        for x in range(r):
            if fishing_ground[x][self.col]:
                self.bucket += fishing_ground[x][self.col][0].size
                fishing_ground[x][self.col] = deque()
                break

def main():
    r, c, m = map(int, input().split())
    fishing_ground = [[deque() for _ in range(c)] for _ in range(r)]

    for _ in range(m):
        row, col, speed, direction, size = map(int, input().split())
        fishing_ground[row-1][col-1] = deque([Shark(row-1, col-1, speed, direction, size)])

    fisher = Human()
    for _ in range(c):
        fisher.move()
        fisher.catchCloestShark(fishing_ground, r, c)
        Shark.moveAllSharks(fishing_ground, r, c)
        Shark.setBiggestShark(fishing_ground, r, c)

    print(fisher.bucket)

main()