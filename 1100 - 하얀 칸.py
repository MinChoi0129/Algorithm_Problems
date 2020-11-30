import sys

chess_board = []

for _ in range(8):
    chess_board.append(sys.stdin.readline().rstrip())

count = 0
for i in [0, 2, 4, 6]:
    for j in [0, 2, 4, 6]:
        if chess_board[i][j] == "F":
            count += 1
for i in [1, 3, 5, 7]:
    for j in [1, 3, 5, 7]:
        if chess_board[i][j] == "F":
            count += 1


print(count)