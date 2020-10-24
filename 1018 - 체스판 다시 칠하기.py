import sys

arr = []
possible = []

def fix(board_64):
    fix_count = 0
    
    if board_64[0][0] == "W":
        for x in [0, 2, 4, 6]:
            for y in [0, 2, 4, 6]:
                if board_64[x][y] != "W":
                    fix_count += 1
                    
        for x in [1, 3, 5, 7]:
            for y in [1, 3, 5, 7]:
                if board_64[x][y] != "W":
                    fix_count += 1
                    
        for x in [0, 2, 4, 6]:
            for y in [1, 3, 5, 7]:
                if board_64[x][y] != "B":
                    fix_count += 1
                    
        for x in [1, 3, 5, 7]:
            for y in [0, 2, 4, 6]:
                if board_64[x][y] != "B":
                    fix_count += 1
                    
                    
    else: # board[0][0] == "B"
        for x in [0, 2, 4, 6]:
            for y in [0, 2, 4, 6]:
                if board_64[x][y] != "B":
                    fix_count += 1
                    
        for x in [1, 3, 5, 7]:
            for y in [1, 3, 5, 7]:
                if board_64[x][y] != "B":
                    fix_count += 1
                    
        for x in [0, 2, 4, 6]:
            for y in [1, 3, 5, 7]:
                if board_64[x][y] != "W":
                    fix_count += 1
                    
        for x in [1, 3, 5, 7]:
            for y in [0, 2, 4, 6]:
                if board_64[x][y] != "W":
                    fix_count += 1
    
    return fix_count

def make_temp_board(n, m):
    temp_list = []
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            for x in range(i, i + 8):
                temp_temp_list = []
                for y in range(j, j + 8):
                    #한개 받아서 임시임시 어펜드
                    temp_temp_list.append(arr[x][y])
                #한줄 받아서 임시 어펜드
                temp_list.append(temp_temp_list)
    return temp_list

n, m = map(int, input().split())
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

