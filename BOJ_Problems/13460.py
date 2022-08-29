from itertools import product as PI
from copy import deepcopy as DC
class EscapedException(Exception):
    def __init__(self, color):
        super().__init__(color)

class Marble:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def moveTo(self, towards, board):
        board[self.x][self.y] = '.'
        if towards == 'E': self.y += 1
        elif towards == 'W': self.y -= 1
        elif towards == 'S': self.x += 1
        else: self.x -= 1

        if type(board[self.x][self.y]) == list:
            board[self.x][self.y].append(self)
        else: board[self.x][self.y] = self
    
    def canMoveTo(self, towards, board):
        if towards == 'E': return (board[self.x][self.y + 1] != '#') and type(board[self.x][self.y + 1]) != Marble
        elif towards == 'W': return (board[self.x][self.y - 1] != '#') and type(board[self.x][self.y - 1]) != Marble
        elif towards == 'S': return (board[self.x + 1][self.y] != '#') and type(board[self.x + 1][self.y]) != Marble
        else: return (board[self.x - 1][self.y] != '#') and type(board[self.x - 1][self.y]) != Marble

def tilt(board, direction, marble_locations):
    if direction in 'E': marble_locations.sort(key=lambda e:e[1], reverse=True)
    elif direction == 'W': marble_locations.sort(key=lambda e:e[1])
    elif direction == 'S': marble_locations.sort(reverse=True)
    else: marble_locations.sort()


    for i in range(2):
        try:
            while True:
                x, y = marble_locations[i]
                current_marble = board[x][y]
                if type(current_marble) == list:
                    marble_locations.pop(0)
                    continue
                if current_marble.canMoveTo(direction, board):
                    current_marble.moveTo(direction, board)
                    marble_locations[i] = [current_marble.x, current_marble.y]
                else:
                    break
        except:
            continue


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
marble_locations = []
goal = [-1, -1]
for x in range(n):
    for y in range(m):
        if board[x][y] in 'RB':
            board[x][y] = Marble(x, y, board[x][y])
            marble_locations.append([x, y])
        elif board[x][y] == 'O':
            goal = [x, y]
            board[x][y] = []

for size in range(1, 11):
    for case in PI("EWSN", repeat = size):
        copied_board = DC(board)
        copied_marble_locations = DC(marble_locations)
        for i in range(len(case)):
            direction = case[i]
            tilt(copied_board, direction, copied_marble_locations)
            if len(board[goal[0]][goal[1]]) == 1: 
                print(i)
                exit(0)
            else:
                break

            # except Exception as e: print(e); exit(0)