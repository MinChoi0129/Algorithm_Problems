from collections import deque

def marbleEscape(board, red_x, red_y, blue_x, blue_y):
    Q, history = deque([(red_x, red_y, blue_x, blue_y, 0)]), {(red_x, red_y, blue_x, blue_y)}
    while Q:
        red_x, red_y, blue_x, blue_y, tilt_count = Q.popleft()
        if tilt_count > 10: print(-1); return
        if board[red_x][red_y] == 'O': print(tilt_count); return

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 4가지 case
            copied_red_x, copied_red_y, copied_blue_x, copied_blue_y = red_x, red_y, blue_x, blue_y        
            
            # move red
            while True:
                copied_red_x += dx; copied_red_y += dy
                if board[copied_red_x][copied_red_y] == '#': copied_red_x -= dx; copied_red_y -= dy; break
                elif board[copied_red_x][copied_red_y] == 'O': break
                
            # move blue
            while True:
                copied_blue_x += dx; copied_blue_y += dy
                if board[copied_blue_x][copied_blue_y] == '#': copied_blue_x -= dx; copied_blue_y -= dy; break
                elif board[copied_blue_x][copied_blue_y] == 'O': break

            if board[copied_blue_x][copied_blue_y] == 'O': continue # 빨간구슬의 골인여부와 관계없이, 파란구슬이 빠졌다면 이 case는 실패.
            
            if copied_red_x == copied_blue_x and copied_red_y == copied_blue_y:
                red_moved_distance, blue_moved_distance = \
                    abs(copied_red_x - red_x) + abs(copied_red_y - red_y), abs(copied_blue_x - blue_x) + abs(copied_blue_y - blue_y)
                
                # 많이 움직인 구슬이 한 걸음 뒤로
                if red_moved_distance < blue_moved_distance: copied_blue_x -= dx; copied_blue_y -= dy
                else: copied_red_x -= dx; copied_red_y -= dy
            
            if (copied_red_x, copied_red_y, copied_blue_x, copied_blue_y) not in history:
                Q.append((copied_red_x, copied_red_y, copied_blue_x, copied_blue_y, tilt_count + 1))
                history.add((copied_red_x, copied_red_y, copied_blue_x, copied_blue_y))
    print(-1)

n, m, board, red_x, red_y, blue_x, blue_y = *map(int, input().split()), [], None, None, None, None
for x in range(n):
    line = list(input())
    for y in range(m):
        if line[y] == 'R': red_x, red_y = x, y
        elif line[y] == 'B': blue_x, blue_y = x, y
    board.append(line)
marbleEscape(board, red_x, red_y, blue_x, blue_y)