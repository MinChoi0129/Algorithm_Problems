n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
answer = -1

for x in range(n):
    for y in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if not (dx == 0 and dy == 0):
                    num = ""
                    row, col = x, y
                    while (0 <= row < n) and (0 <= col < m):
                        num += board[row][col]
                        if int(num) == int(int(num) ** 0.5) ** 2:
                            answer = max(answer, int(num))
                        row += dx; col += dy
print(answer)