import sys

def fix(board_64):
    
    fix_count1 = 0
    fix_count2 = 0

    # 좌측 상단을 W로 시작하기
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

    # 좌측상단을 B로 시작하기
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
    global arr
    
    all_boards = []
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            temp_board = [] # 8 * 8 한 판 받을 것
            for x in range(i, i + 8):
                temp_list = [] # 8 * 1 한 줄 받을 것
                for y in range(j, j + 8):
                    temp_list.append(arr[x][y])
                temp_board.append(temp_list)
                
            all_boards.append(temp_board) # 8 * 8 보드 한 판 담기
            
    return all_boards

n, m = map(int, input().split())

arr = []
possible = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

all_boards = make_boards(n, m)

for board in all_boards:
    possible.append(fix(board))

print(min(possible))