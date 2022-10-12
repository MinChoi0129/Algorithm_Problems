class Board:
    def __init__(self, board_data):
        self.board = board_data

    def getCounterClockwiseShellRoatatedBoard(self):
        n = len(self.board)
        array = self.board
        left_top = [0, 0]
        right_top = [0, m-1]
        left_bot = [n-1, 0]
        right_bot = [n-1, m-1]

        while (left_top[0] <= right_bot[0]) and (left_top[1] <= right_bot[1]):
            # 서쪽 방향 이동
            tmp_left_top = array[left_top[0]][left_top[1]]
            y = left_top[1]
            while y < right_top[1]:
                array[left_top[0]][y] = array[left_top[0]][y+1]
                y += 1

            # 남쪽 방향 이동
            tmp_left_bot = array[left_bot[0]][left_bot[1]]
            x = left_bot[0]
            while x > left_top[0]:
                array[x][left_bot[1]] = array[x-1][left_bot[1]]
                x -= 1
            array[x+1][left_bot[1]] = tmp_left_top

            # 동쪽 방향 이동
            tmp_right_bot = array[right_bot[0]][right_bot[1]]
            y = right_bot[1]
            while y > left_bot[1]:
                array[left_bot[0]][y] = array[left_bot[0]][y-1]
                y -= 1
            array[left_bot[0]][y+1] = tmp_left_bot

            # 북쪽 방향 이동
            x = right_top[0]
            while x < right_bot[0]:
                array[x][right_top[1]] = array[x+1][right_top[1]]
                x += 1
            array[x-1][right_bot[1]] = tmp_right_bot
            left_top[0] += 1
            left_top[1] += 1

            right_top[0] += 1
            right_top[1] -= 1

            left_bot[0] -= 1
            left_bot[1] += 1

            right_bot[0] -= 1
            right_bot[1] -= 1

            
        return Board(array)
    
    def __str__(self):
        result = ""
        for line in self.board:
            for element in line:
                result += str(element) + " "
            result += "\n"
        return result

n, m, r = map(int, input().split())
board = Board([[*map(int, input().split())] for _ in range(n)])

for _ in range(r % (2 * n + 2 * (m-2))):
    board = board.getCounterClockwiseShellRoatatedBoard()
        
print(board)