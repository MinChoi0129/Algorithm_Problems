import sys
class Shark:
    def __init__(self, speed, direction, size):
        self.speed = speed
        self.direction = direction
        self.size = size
    
    def isFrontWall(self):
        return True if self.
    def move(self, times):
        if not self.isFrontWall():
        if self.direction == 'n':
        else:pass

class Human:
    def __init__(self, col):
        self.bucket = 0
        self.col = col
    def move(self):
        if self.col + 1 > c: raise IndexError()
        self.col += 1
    def catchCloestShark(self, r):
        for x in range(r):
            if type(fishing_ground[r][c]) == Shark:
                self.bucket += fishing_ground[r][c].size
                fishing_ground[r][c] = 0
                break

input = lambda : sys.stdin.readline().rstrip()
r, c, m = map(int, input().split())
fishing_ground = [[0] * c for _ in range(r)]
for _ in range(m):
    r, c, speed, direction, size = map(int, input().split())
    fishing_ground[r-1][c-1] = Shark(speed, direction, size)