import sys

def fix(board_64):
    
    fix_count1 = 0
    fix_count2 = 0
   
    for x in [0, 2, 4, 6]:
        for y in [0, 2, 4, 6]:
            if board_64[x][y] != "W":
                fix_count1 += 1
                
    for x in [1, 3, 5, 7]:
        for y in [1, 3, 5, 7]:
            if board_64[x][y] != "W":
                fix_count1 += 1
                
    for x in [0, 2, 4, 6]:
        for y in [1, 3, 5, 7]:
            if board_64[x][y] != "B":
                fix_count1 += 1
                
    for x in [1, 3, 5, 7]:
        for y in [0, 2, 4, 6]:
            if board_64[x][y] != "B":
                fix_count1 += 1

                
    for x in [0, 2, 4, 6]:
        for y in [0, 2, 4, 6]:
            if board_64[x][y] != "B":
                fix_count2 += 1
                
    for x in [1, 3, 5, 7]:
        for y in [1, 3, 5, 7]:
            if board_64[x][y] != "B":
                fix_count2 += 1
                
    for x in [0, 2, 4, 6]:
        for y in [1, 3, 5, 7]:
            if board_64[x][y] != "W":
                fix_count2 += 1
                
    for x in [1, 3, 5, 7]:
        for y in [0, 2, 4, 6]:
            if board_64[x][y] != "W":
                fix_count2 += 1

    return min(fix_count1, fix_count2)

def make_boards(n, m):
    all_board = []
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            temp_board = []
            for x in range(i, i + 8):
                temp_list = []
                for y in range(j, j + 8):
                    #한개 받아서 임시임시 어펜드
                    temp_list.append(arr[x][y])
                #한줄 받아서 임시 어펜드
                temp_board.append(temp_list)
            all_board.append(temp_board)        
            # 8 * 8 1개 완성
    return all_board

n, m = map(int, input().split())

arr = []
possible = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

all_boards = make_boards(n, m)

for i in range(len(all_boards)):
    possible.append(fix(all_boards[i]))

print(min(possible))
