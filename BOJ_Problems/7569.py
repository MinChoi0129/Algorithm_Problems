from collections import deque
m, n, h = map(int, input().split())
tomato_box = [[[*map(int, input().split())] for _ in range(n)] for _ in range(h)] # z, x, y 순서대로(n층, 가로, 세로)
Q = deque([z, x, y] for z in range(h) for y in range(m) for x in range(n) if tomato_box[z][x][y] == 1)

while Q:
    z, x, y = Q.popleft()
    for dx, dy, dz in [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        new_z, new_x, new_y = z+dz, x+dx, y+dy
        if not (0 <= new_z < h and 0 <= new_x < n and 0 <= new_y < m): continue
        if tomato_box[new_z][new_x][new_y] == 0:
            Q.append([new_z, new_x, new_y])
            tomato_box[new_z][new_x][new_y] = tomato_box[z][x][y] + 1

def tomato_calculator(min_days):
    for tomato_board in tomato_box:
        for tomato_line in tomato_board:
            for tomato_days in tomato_line:
                if tomato_days == 0: print(-1); return
                else: min_days = max(min_days, tomato_days)
    print(min_days - 1)
tomato_calculator(0)