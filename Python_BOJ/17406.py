from copy import deepcopy
from itertools import permutations as P
from collections import deque as D

class Board:
    def __init__(self, board_data):
        self.board = board_data
    
    def getBoardMin(self):
        return min([sum(line) for line in self.board])

    
    def getClockwiseShellRoatatedBoard(self):
        pass

    def getPartialBoard(self, r, c, s): # given r, c should be index
        return Board([[self.board[x][y] for y in range(c-s, c+s+1)] for x in range(r-s, r+s+1)])

    def getCombinedBoard(self, partialBoard, r, c, s): # given r, c should be index
        combined_board = deepcopy(self.board)
        for x in range(r-s, r+s+1):
            for y in range(c-s, c+s+1):
                combined_board[x][y] = partialBoard.board[x-r+s][y-c+s]
        return Board(combined_board)
    
    def __str__(self):
        result = ""
        for line in self.board:
            for element in line:
                result += str(element) + " "
            result += "\n"
        return result

n, m, k = map(int, input().split())
board = Board([[*map(int, input().split())] for _ in range(n)])

board_minimums = []
for combi in P([[*map(int, input().split())] for _ in range(k)], k):
    for r, c, s in combi:
        board_minimums.append(board.getCombinedBoard(board.getPartialBoard(r-1, c-1, s).getClockwiseShellRoatatedBoard(), r-1, c-1, s).getBoardMin())
        
print(min(board_minimums))