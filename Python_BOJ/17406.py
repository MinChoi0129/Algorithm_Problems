from copy import deepcopy
from itertools import permutations as P

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    def __init__(self, matrix):
        self.board = matrix

    def getBoardMin(self):
        return min([sum(line) for line in self.board])

    def getPartialBoard(self, r, c, s): # given r, c should be index
        return Board([[self.board[x][y] for y in range(c-s, c+s+1)] for x in range(r-s, r+s+1)])

    def setCombinedBoard(self, partialBoard, r, c, s): # given r, c should be index
        for x in range(r-s, r+s+1):
            for y in range(c-s, c+s+1):
                self.board[x][y] = partialBoard.board[x-r+s][y-c+s]
    
    # https://velog.io/@dasd412/%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-4-%EB%B0%B1%EC%A4%80-17406-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    def setShellRoatatedClockwise(self):
        size = len(self.board)
        lu, rd = Point(0, 0), Point(size-1, size-1)

        while lu.x != rd.x and lu.y != rd.y:
            tmp_ru = self.board[lu.x][rd.y]

            # 동쪽 방향 이동
            y = rd.y
            while y > lu.y:
                self.board[lu.x][y] = self.board[lu.x][y - 1]
                y -= 1
            tmp_rd = self.board[rd.x][rd.y]

            # 남쪽 방향 이동
            x = rd.x
            while x > lu.x:
                self.board[x][rd.y] = self.board[x - 1][rd.y]
                x -= 1
            self.board[x + 1][rd.y] = tmp_ru

            # 서쪽 방향 이동
            tmp_ld = self.board[rd.x][lu.y]

            y = lu.y
            while y < rd.y:
                self.board[rd.x][y] = self.board[rd.x][y + 1]
                y += 1
            self.board[rd.x][y - 1] = tmp_rd

            # 북쪽 이동
            x = lu.x
            while x < rd.x:
                self.board[x][lu.y] = self.board[x + 1][lu.y]
                x += 1
            self.board[x - 1][lu.y] = tmp_ld

            # 맨 왼쪽과 맨 오른쪽의 좌표를 각각 수정해줍니다.
            lu.x += 1; lu.y += 1; rd.x -= 1; rd.y -= 1

n, m, k = map(int, input().split())
board = Board([[*map(int, input().split())] for _ in range(n)])
mins = []
for combi in P([[*map(int, input().split())] for _ in range(k)], k):
    new_board = deepcopy(board)
    for r, c, s in combi:
        partial_board = new_board.getPartialBoard(r-1, c-1, s)
        partial_board.setShellRoatatedClockwise()
        new_board.setCombinedBoard(partial_board, r-1, c-1, s)
    mins.append(new_board.getBoardMin())
        
print(min(mins))