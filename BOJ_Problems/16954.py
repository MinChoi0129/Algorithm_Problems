from collections import deque


def moveCharacter(board, x, y, direction):
    """
    direction
    0: 제자리, 1: N, 2: NE, 3: E, ... , 7: W, 8: NW
    """
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]
    new_x, new_y = x + dx[direction], y + dy[direction]
    if 0 <= new_x < 8 and 0 <= new_y < 8:
        if board[new_x][new_y] == "." or board[new_x][new_y] == "M":
            board[x][y] = "."
            board[new_x][new_y] = "M"
            return board, new_x, new_y
        else:
            raise Exception("Wall Exists")
    else:
        raise Exception("Out of Boundary")


def moveWalls(board, positions):
    wall_positions = []
    for x, y in positions:
        new_x, new_y = x + 1, y
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            if board[new_x][new_y] == "M":
                raise Exception("Character Exists")
            else:  # 벽 이동
                board[x][y] = "."
                board[new_x][new_y] = "#"
                wall_positions.append((new_x, new_y))
        else:  # 벽 사라짐
            pass
    return board, wall_positions


def BFS(Q):
    while Q:
        new_board, wall_positions, new_x, new_y = Q.popleft()
        for direction in range(9):
            try:
                new_board, new_x, new_y = moveCharacter(
                    new_board, new_x, new_y, direction
                )
                new_board, new_wall_positions = moveWalls(new_board, wall_positions)
                if new_x == 0 and new_y == 7:
                    return 1
                Q.append((new_board, new_wall_positions, new_x, new_y))
            except:
                continue
    return 0


board, wall_positions = [], []
for x in range(8):
    line = list(input())
    for y in range(8):
        if line[y] == "#":
            wall_positions.append((x, y))
    board.append(line)

x, y = 7, 0
board[x][y] = "M"
Q = deque([(board, wall_positions, x, y)])
print(BFS(Q))
