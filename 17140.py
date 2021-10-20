r, c, k = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(3)]
global_timer = 0

def special_sorter(board, sorting_mode):
    global global_timer
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
            print(list(checker.items()))
            new_line = sorted(list(checker.items()), key = lambda x : (x[1], x[0]))
            for i in range(len(new_line)):
                line[i] = new_line[i]
        
        # 삐죽빼죽한 상태
        len_longest_line = 0
        for line in board:
            len_longest_line = max(len_longest_line, len(line))
        
        for line in board:
            for _ in range(len_longest_line - len(line)):
                line.append(0)
    
    elif sorting_mode == 'C':
        global_timer += 1


while True:
    if global_timer >= 100:
        if board[r - 1][c - 1] != k:
            print(-1)
            break
    else:
        if board[r - 1][c - 1] == k:
            print(global_timer)
            break
        else:
            width, height = len(board[0]), len(board)
            if height >= width:
                special_sorter(board, 'R')
            else:
                special_sorter(board, 'C')