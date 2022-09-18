def getBoardType(board):
    default_type = board[0][0]
    for line in board:
        for element in line:
            if element != default_type: return None
    return default_type

def countBoardTypes(current_board):
    board_type = getBoardType(current_board)
    if board_type == None:
        size = len(current_board); cut_size = size // 3
        for k in range(3):
            new_board = []
            for i in range(size):
                line = [current_board[i][j] for j in range(k * cut_size, k * cut_size + cut_size)]
                new_board.append(line)
                if (i + 1) % cut_size == 0: countBoardTypes(new_board); new_board = []
    else: board_types[board_type] += 1

board, board_types = [[*map(int, input().split())] for _ in range(int(input()))], [0, 0, 0]
countBoardTypes(board)
for board_type in [-1, 0, 1]: print(board_types[board_type])