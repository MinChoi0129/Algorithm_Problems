from copy import deepcopy as DC

r, c, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(3)]
global_timer = 0

def rotate_90_degree(arr, clockwise):
    if clockwise:        
        return list(map(list, zip(*reversed([*arr]))))
    else:
        return [list(i) for i in reversed(tuple(zip(*arr)))]

def special_sorter(sorting_mode):
    global global_timer, board
    if sorting_mode == 'R':
        global_timer += 1
        for line in board: # 행 정렬
            checker = dict()
            for num in line:
                if num == 0:
                    continue
                if num not in checker:
                    checker[num] = 1
                else:
                    checker[num] += 1
            new_line = []
            for i in sorted(list(checker.items()), key = lambda x : (x[1], x[0])):
                new_line += list(i)
            line.clear()
            for i in range(len(new_line) % 100):
                line.append(new_line[i])
        
        # 삐죽빼죽한 상태
        len_longest_line = 0
        for line in board:
            len_longest_line = max(len_longest_line, len(line))
                  
        for line in board:
            line : list
            for _ in range(len_longest_line - len(line)):
                line.append(0)
    
    elif sorting_mode == 'C':
        global_timer += 1
        new_board = rotate_90_degree(DC(board), clockwise = False)
        for line in new_board: # 행 정렬
            checker = dict()
            for num in line:
                if num == 0:
                    continue
                if num not in checker:
                    checker[num] = 1
                else:
                    checker[num] += 1
            new_line = []
            for i in sorted(list(checker.items()), key = lambda x : (x[1], x[0])):
                new_line += list(i)
            line.clear()
            for i in range(len(new_line) % 100):
                line.append(new_line[i])
        
        # 삐죽빼죽한 상태
        len_longest_line = 0
        for line in new_board:
            len_longest_line = max(len_longest_line, len(line))
                  
        for line in new_board:
            line : list
            for _ in range(len_longest_line - len(line)):
                line.append(0)
        
        board = rotate_90_degree(new_board, clockwise = True)

while True:
    if global_timer > 100:
        if not (len(board) >= r and len(board[0]) >= c):
            print(-1)
            break
        if board[r - 1][c - 1] != k:
            print(-1)
            break
    else:
        if (len(board) >= r and len(board[0]) >= c) and board[r - 1][c - 1] == k:
            print(global_timer)
            break
        else:
            width, height = len(board[0]), len(board)
            if height >= width:
                special_sorter('R')
            else:
                special_sorter('C')