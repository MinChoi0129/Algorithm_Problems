class Board:
    def __init__(self, board_data):
        self.board = board_data
        self.size = len(self.board)

    def isAllSameNumber(self):
        start_num = self.board[0][0]
        for line in self.board:
            for element in line:
                if element != start_num:
                    return False
        return True

    def getFourDividedBoards(self):
        board_1, board_2 = [], []
        for x in range(self.size // 2):
            line_1, line_2 = [], []
            for y in range(self.size // 2): line_1.append(self.board[x][y])
            for y in range(self.size // 2, self.size): line_2.append(self.board[x][y])
            board_1.append(line_1); board_2.append(line_2)

        board_3, board_4 = [], []
        for x in range(self.size // 2, self.size):
            line_3, line_4 = [], []
            for y in range(self.size // 2): line_3.append(self.board[x][y])
            for y in range(self.size // 2, self.size): line_4.append(self.board[x][y])
            board_3.append(line_3); board_4.append(line_4)
        
        return [Board(b) for b in [board_1, board_2, board_3, board_4]]
        
    def print(self):
        if self.isAllSameNumber(): print(self.board[0][0], end='')
        else:
            print('(', end='')
            for piece in self.getFourDividedBoards(): piece.print()
            print(')', end='')
            
n = int(input())
Board([[*map(int, list(input()))] for _ in range(n)]).print()