def rotated(board):
    return [[board[y][x] for y in range(len(board))] for x in range(len(board[0]) - 1, -1, -1)]

def getCleanBoard():
    idx_x_edited, idx_y_edited = False, False
    board, idx_x, idx_y = [], -1, -1
    for i in range(10):
        line = list(input())
        if line != list("0000000000"):
            board.append(list(line))
            if not idx_x_edited:
                idx_x = i
                idx_x_edited = True
    tmp_board = rotated(rotated(rotated(board)))
    new_board = []
    delete_count = 0

    for line in tmp_board:
        if line == ['0'] * (len(tmp_board[0])): delete_count += 1
        else:
            new_board.append(line)
            if not idx_y_edited:
                idx_y = delete_count + 1
                idx_y_edited = True
    
    return [rotated(tmp_board), idx_x, idx_y]

def isRightTriangle(board):
    a, b = len(board), len(board[0])
    a, b = min(a, b), max(a, b) # 짧은게 a 긴게 b
    return True if a * 2 == b + 1 else False

def getTypeOfRightTriangle(board):
    first_line = board[0]
    if first_line[len(first_line) // 2] == '1': return 'u'
    elif first_line.count('1') == len(first_line): return 'd'
    elif first_line[0] == '1': return 'r'
    elif first_line[-1] == '1': return 'l'

board, idx_x, idx_y = getCleanBoard()
if isRightTriangle(board):
    triangle_type = getTypeOfRightTriangle(board)
    w, h = len(board[0]), len(board)
    if triangle_type == 'u':
        answer = [(idx_x, idx_y + w // 2), (idx_x + (h-1), idx_y), (idx_x + (h-1), idx_y + (w-1))]

    elif triangle_type == 'd':
        pass

    elif triangle_type == 'l':
        

    else: # 'r'
        pass

else: print(0)