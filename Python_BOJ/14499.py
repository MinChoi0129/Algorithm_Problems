n, m, x, y, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
commands = [*map(int, input().split())]

class Dice:
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.top, self.bottom, self.left, self.right, self.front, self.back = 0, 0, 0, 0, 0, 0
    
    def roll(self, direction):
        if not self.check(direction):
            return

        # 이동 및 상하좌우전후 교환
        if direction == 1: # 동
            self.y += 1
            self.top, self.bottom, self.left, self.right = self.left, self.right, self.bottom, self.top
        elif direction == 2: # 서
            self.y -= 1
            self.top, self.bottom, self.left, self.right = self.right, self.left, self.top, self.bottom
        elif direction == 3: # 남
            self.x -= 1
            self.top, self.bottom, self.front, self.back = self.back, self.front, self.top, self.bottom
        elif direction == 4: # 북
            self.x += 1
            self.top, self.bottom, self.front, self.back = self.front, self.back, self.bottom, self.top
        
        # 교환 및 변경
        if board[self.x][self.y] == 0:
            board[self.x][self.y] = self.bottom
        else:
            self.bottom = board[self.x][self.y]
            board[self.x][self.y] = 0
            
        print(self.top)
        
    
    def check(self, direction):
        if direction == 1:
            if self.y + 1 == m:
                return False
        elif direction == 2:
            if self.y - 1 == -1:
                return False
        elif direction == 3:
            if self.x - 1 == -1:
                return False
        elif direction == 4:
            if self.x + 1 == n:
                return False           
        return True
 
dice = Dice(x, y)   
for cmd in commands:
    dice.roll(cmd)