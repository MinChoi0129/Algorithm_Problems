n, r, c = map(int, input().split())
board = [[0] * (2 ** n) for _ in range(2 ** n)]
board[r][c] = 1
answer = 0
if n == 1: print(answer)
else:
    while n:
        if r < 2 ** (n-1):
            if c >= 2 ** (n-1): # 1사분면
                k = 1
                board = [[board[x][y] for y in range(2 ** (n-1), 2 ** n)] for x in range(2 ** (n-1))]
            else: # 2사분면
                k = 2
                board = [[board[x][y] for y in range(2 ** (n-1))] for x in range(2 ** (n-1))]
        else:
            if c < 2 ** (n-1): # 3사분면
                k = 3
                board = [[board[x][y] for y in range(2 ** (n-1))] for x in range(2 ** (n-1), 2 ** n)]
            else: # 4사분면
                k = 4
                board = [[board[x][y] for y in range(2 ** (n-1), 2 ** n)] for x in range(2 ** (n-1), 2 ** n)]
                
        board_size = len(board)
        for x in range(board_size):
            r_c_changed = False
            for y in range(board_size):
                if board[x][y] == 1:
                    r, c = x, y
                    r_c_changed = True
                    break
            if r_c_changed: break
        answer += (2 ** (2*n-2) * (k - 1))
        n -= 1

    print(answer)