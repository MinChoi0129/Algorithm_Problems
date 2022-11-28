from copy import deepcopy as DC

directions = {0: [-1, 0], 1: [-1, -1], 2: [0, -1], 3: [1, -1], 4: [1, 0], 5: [1, 1], 6: [0, 1], 7: [-1, 1]}

class Fish:
    def __init__(self, x, y, size, direction):
        self.x, self.y, self.size = x, y, size
        self.direction = directions[direction-1]
        self.turn_count = 0

    def canMove(self):
        new_x, new_y = self.x + self.direction[0], self.y + self.direction[1]
        return False if (not (0 <= new_x < 4 and 0 <= new_y < 4)) or type(board[new_x][new_y]) == Shark else True
    
    def turn(self):
        self.direction = (self.direction + 1) % 8
        self.turn_count += 1

    def move(self):
        if self.canMove():
            new_x, new_y = self.x + self.direction[0], self.y + self.direction[1]
            board[self.x][self.y], board[new_x][new_y] = board[new_x][new_y], board[self.x][self.y]
        else:
            if self.turn_count < 8:
                self.turn()
                self.move()
            else:
                return


class Shark:
    def __init__(self, x, y, size, direction):
        self.x, self.y, self.size = x, y, size
        self.direction = direction
    
    def eatFish(self):
        for i in range(len(fishes)):
            if fishes[i].size == board[self.x][self.y].size:
                fishes.pop(i)
                break
        
        self.size += board[self.x][self.y].size
        self.direction = board[self.x][self.y].direction
        board[self.x][self.y] = 0
    
    def move(self, board):
        new_x, new_y = self.x + self.direction[0], self.y + self.direction[1]

        self.eatFish()

board = [[] * 4 for _ in range(4)]
fishes = []
for x in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    fish_1 = Fish(x, 0, a1, b1)
    fish_2 = Fish(x, 1, a2, b2)
    fish_3 = Fish(x, 2, a3, b3)
    fish_4 = Fish(x, 3, a4, b4)
    board[x] = [fish_1, fish_2, fish_3, fish_4]
    fishes.extend([fish_1, fish_2, fish_3, fish_4])

board[0][0] = Shark(0, 0, board[0][0].size, board[0][0].direction)
fishes.pop(0)
fishes.sort(key = lambda obj: obj.size)
shark = board[0][0]

for fish in fishes:
    fish.move()
shark.move()
print()