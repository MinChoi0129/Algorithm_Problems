r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
Q, answer = set([(0, 0, board[0][0])]), 1
while Q:
    x, y, present_txt = Q.pop()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x+dx, y+dy
        if 0 <= new_x < r and 0 <= new_y < c and board[new_x][new_y] not in present_txt:
            new_txt = present_txt + board[new_x][new_y]
            Q.add((new_x, new_y, new_txt)); answer = max(answer, len(new_txt))
print(answer)