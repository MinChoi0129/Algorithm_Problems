directions = {0: 'N', 1: 'NW', 2: 'W', 3: 'SW', 4: 'S', 5: 'SE', 6: 'E', 7: 'NE'}

class Fish:
    def __init__(self, x, y, size, direction):
        self.x, self.y, self.size = x, y, size
        self.direction = directions[direction]

class Shark:
    def __init__(self, x, y, size, direction):
        self.x, self.y, self.size = x, y, size
        self.direction = directions[direction]