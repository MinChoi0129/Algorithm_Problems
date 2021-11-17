board = [[None for _ in range(15)] for _ in range(5)]

for i in range(5):
    txt = input()
    for t in range(len(txt)):
        board[i][t] = txt[t]

for y in range(15):
    for x in range(5):
        if board[x][y] != None:
            print(board[x][y], end = "")
print()