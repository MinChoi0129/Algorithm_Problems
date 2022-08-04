from copy import deepcopy
n = int(input())
board = [[False] * n for _ in range(n)]

def tryNQueen(x, y, board, n):
    for i in range(n):
        board[i][y] = True
        board[x][i] = True
            
    ld_x, ld_y, lu_x, lu_y, rd_x, rd_y, ru_x, ru_y = x, y, x, y, x, y, x, y
    while 0 <= ld_x < n and 0 <= ld_y < n:
        if board[ld_x][ld_y] != 'Q': board[ld_x][ld_y] = True
        ld_x += 1; ld_y -= 1

    while 0 <= lu_x < n and 0 <= lu_y < n:
        if board[lu_x][lu_y] != 'Q': board[lu_x][lu_y] = True
        lu_x -= 1; lu_y -= 1
        
    while 0 <= rd_x < n and 0 <= rd_y < n:
        if board[rd_x][rd_y] != 'Q': board[rd_x][rd_y] = True
        rd_x += 1; rd_y += 1
        
    while 0 <= ru_x < n and 0 <= ru_y < n:
        if board[ru_x][ru_y] != 'Q': board[ru_x][ru_y] = True
        ru_x -= 1; ru_y += 1
    
    board[x][y] = 'Q'
    
    for row in range(n):
        for col in range(n):
            if board[row][col] == False:
                tryNQueen(row, col, board, n)
    
    return board

def isNQueenStatus(board, n):
    queen_count = 0
    for line in board:
        for element in line:
            if element == 'Q': queen_count += 1
    return True if queen_count == n else False

count = 0
for x in range(n):
    for y in range(n):
        tmp_board = tryNQueen(x, y, deepcopy(board), n)
        if isNQueenStatus(tmp_board, n):
            count += 1
print(count)