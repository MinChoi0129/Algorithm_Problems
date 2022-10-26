board = [[*map(int, input().split())] for _ in range(9)]
max_value = -1
ans_x, ans_y = None, None
for x in range(9):
    for y in range(9):
        value = board[x][y]
        if value > max_value:
            ans_x, ans_y = x+1, y+1
            max_value = value
print(max_value)
print(ans_x, ans_y)