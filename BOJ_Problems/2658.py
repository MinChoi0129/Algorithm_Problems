def rotated(board): return [[board[y][x] for y in range(len(board))] for x in range(len(board[0]) - 1, -1, -1)]

def getCleanBoard():
    board, x, y, is_x_fixed, is_y_fixed = [], None, None, False, False

    for idx in range(10):
        line = input()
        if line != "0000000000":
            board.append(list(line))
            if not is_x_fixed: x = idx; is_x_fixed = True

    if board:
        tmp_board, new_board = rotated(rotated(rotated(board))), []
        for idx in range(10):
            line = tmp_board[idx]
            if line != ['0'] * (len(tmp_board[idx])):
                new_board.append(line)
                if not is_y_fixed: y = idx; is_y_fixed = True
        return [rotated(new_board), x, y, len(new_board), len(new_board[0])]

    else: return [[], None, None, 0, 0]

def isRightTriangle(board, w, h):
    if h <= 1: return [False, None]

    a, b = min(w, h), max(w, h)
    if a == b: all_triangles = [[['1']*i+['0']*(a-i) for i in range(1, a+1)]]
    else: all_triangles = [[['0']*(a-i)+['1']*(2*i-1)+['0']*(a-i) for i in range(1, a+1)]]

    for _ in range(3): all_triangles.append(rotated(all_triangles[-1]))

    if board in all_triangles: return [True, '1234'] if a == b else [True, 'EWSN']
    else: return [False, None]

def getTypeOfRightTriangle(board, triangle_type, w):
    if triangle_type == 'EWSN': # 동서남북
        if board[0] == list('0'*((w-1)//2)+'1'+'0'*((w-1)//2)): return 'n'
        elif board[0] == list('1'+'0'*(w-1)): return 'e'
        elif board[0] == list('0'*(w-1)+'1'): return 'w'
        elif board[0] == list('1'*w): return 's'
    else: # 1234사분면
        if board[0][-1] == '0': return 'sw'
        elif board[-1][-1] == '0': return 'nw'
        elif board[0][0] == '0': return 'se'
        elif board[-1][0] == '0': return 'ne'

board, start_x, start_y, w, h = getCleanBoard()
is_right_triangle, triangle_type = isRightTriangle(board, w, h)

if is_right_triangle:
    triangle_type = getTypeOfRightTriangle(board, triangle_type, w)
    if   triangle_type == 'n': answer = [(start_x,start_y+w//2),(start_x+(h-1),start_y),(start_x+(h-1),start_y+(w-1))]
    elif triangle_type == 's': answer = [(start_x,start_y),(start_x,start_y+(w-1)),(start_x+(h-1),start_y+w//2)]
    elif triangle_type == 'w': answer = [(start_x,start_y+(w-1)),(start_x+h//2,start_y),(start_x+(h-1),start_y+(w-1))]
    elif triangle_type == 'e': answer = [(start_x,start_y),(start_x+h//2,start_y+(w-1)),(start_x+(h-1),start_y)]
    elif triangle_type == 'sw': answer= [(start_x,start_y),(start_x+(h-1),start_y),(start_x+(h-1),start_y+(w-1))]
    elif triangle_type == 'nw': answer= [(start_x,start_y),(start_x,start_y+(w-1)),(start_x+(h-1),start_y)]
    elif triangle_type == 'se': answer= [(start_x,start_y+(w-1)),(start_x+(h-1),start_y),(start_x+(h-1),start_y+(w-1))]
    elif triangle_type == 'ne': answer= [(start_x,start_y),(start_x,start_y+(w-1)),(start_x+(h-1),start_y+(w-1))]
    for x, y in answer: print(x+1, y+1)
else: print(0)