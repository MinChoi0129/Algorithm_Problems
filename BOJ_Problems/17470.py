def rotated(arr_2d, angle=90):
    if angle == 90: return list(map(list, zip(*arr_2d[::-1])))
    elif angle == 270: return list(map(list, zip(*arr_2d)))[::-1]

def getCommandAppliedBoard(board, n, m, locations):
    a, b, c, d = [0, 0], [n-1, 0], [0, m-1], [n-1, m-1]
    if locations == [a, b, c, d]: return board
    elif locations == [a, c, b, d]: return rotated(board[::-1])
    elif locations == [b, a, d, c]: return board[::-1]
    elif locations == [b, d, a, c]: return rotated(board)
    elif locations == [c, a, d, b]: return rotated(board, 270)
    elif locations == [c, d, a, b]: return [line[::-1] for line in board]
    elif locations == [d, b, c, a]: return rotated([line[::-1] for line in board])
    elif locations == [d, c, b, a]: return rotated(rotated(board))

def getNewlyEditedBoard(board, n, m, mode):
    new_board = [[None] * m for _ in range(n)]

    # G1 <-> G2
    for x in range(0, n // 2):
        for y in range(0, m // 2):
            if mode == '5': new_board[x][y + m // 2] = board[x][y]
            else: new_board[x][y] = board[x][y + m // 2]

    # G2 <-> G3
    for x in range(0, n // 2):
        for y in range(m // 2, m):
            if mode == '5': new_board[x + n // 2][y] = board[x][y]
            else: new_board[x][y] = board[x + n // 2][y]

    # G3 <-> G4
    for x in range(n // 2, n):
        for y in range(m // 2, m):
            if mode == '5': new_board[x][y - m // 2] = board[x][y]
            else: new_board[x][y] = board[x][y - m // 2]
    
    # G4 <-> G1
    for x in range(n // 2, n):
        for y in range(0, m // 2):
            if mode == '5': new_board[x - n // 2][y] = board[x][y]
            else: new_board[x][y] = board[x - n // 2][y]

    return new_board


n, m, r = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
commands = ''.join(input().split())

# 원상복구되는 명령은 삭제
while '11' in commands or '22' in commands or '34' in commands or '43' in commands or '56' in commands or '65' in commands:
    while '11' in commands: commands = commands.replace('11', '')
    while '22' in commands: commands = commands.replace('22', '')
    while '34' in commands: commands = commands.replace('34', '')
    while '43' in commands: commands = commands.replace('43', '')
    while '56' in commands: commands = commands.replace('56', '')
    while '65' in commands: commands = commands.replace('65', '')

# 초기 꼭짓점좌표(좌상, 좌하, 우상, 우하)
lu, ld, ru, rd = [0, 0], [n-1, 0], [0, m-1], [n-1, m-1]

# 
for command in commands: # 명령에 따라 원본배열 움직이지 않고 꼭짓점좌표만 움직여줌.
    if command == '1': lu, ld = ld, lu; ru, rd = rd, ru
    elif command == '2': lu, ru = ru, lu; ld, rd = rd, ld
    elif command == '3': lu, ru, rd, ld = ld, lu, ru, rd
    elif command == '4': lu, ru, rd, ld = ru, rd, ld, lu
    elif command in '56': # 1, 2, 3, 4일땐 원본을 수정하지 않았지만 5, 6은 직접 수정해줌
        board = getCommandAppliedBoard(board, n, m, locations = [lu, ld, ru, rd]) # 마지막 꼭짓점 좌표에 맞게 원본을 바꿔줌
        lu, ld, ru, rd = [0, 0], [n-1, 0], [0, m-1], [n-1, m-1] # 원본을 수정했으니 새롭게 꼭짓점 설정해줌.
        board = getNewlyEditedBoard(board, n, m, command) # 5 or 6 명령 실행.

# 마지막 명령이 1,2,3,4 중 하나로 끝났다면 최종적용.
board = getCommandAppliedBoard(board, n, m, locations = [lu, ld, ru, rd])

# 출력
for line in board:
    print(*line)