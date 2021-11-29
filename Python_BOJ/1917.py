from copy import deepcopy as DC

def setBoards():
    tmp_boards = []
    tmp_board = []
    for i in range(18):
        line = input().split()
        if line != ['0', '0', '0', '0', '0', '0']:
            tmp_board.append(line)
        if (i + 1) % 6 == 0:
            tmp_boards.append(tmp_board)
            tmp_board = []
    
    for i in range(3):
        # copied_board1 = rotated(DC(tmp_boards[i]))
        # copied_board2 = rotated(DC(tmp_boards[i]))
        # copied_board2 = rotated(copied_board2)
        # copied_board2 = rotated(copied_board2)
        
        tmp_board_1, tmp_board_2 = [], []        
        for j in range(len(copied_board1)):
            if copied_board1[j] != ['0', '0', '0', '0', '0', '0']:
                tmp_board_1.append(copied_board1[j])
            if copied_board2[j] != ['0', '0', '0', '0', '0', '0']:
                tmp_board_2.append(copied_board2[j])
        copied_board1, copied_board2 = tmp_board_1, tmp_board_2
    
    


def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

boards = setBoards()