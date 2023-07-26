from collections import deque

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]


def BFS(Q: deque):
    while Q:
        current_character_x, current_character_y = Q.popleft()

        # 캐릭터 이동
        new_character_positions = set()
        for direction in range(9):
            new_character_x, new_character_y = (
                current_character_x + dx[direction],
                current_character_y + dy[direction],
            )
            if (new_character_x, new_character_y) == (0, 7):
                return 1
            elif (
                0 <= new_character_x < 8
                and 0 <= new_character_y < 8
                and (new_character_x, new_character_y) not in wall_positions
                and (new_character_x, new_character_y) not in visited;
            ):
                new_character_positions.add((new_character_x, new_character_y))

        # 벽 이동
        new_wall_positions = set()
        for wall_x, wall_y in wall_positions:
            new_wall_x, new_wall_y = wall_x + 1, wall_y
            if 0 <= new_wall_x < 8 and 0 <= new_wall_y < 8:
                new_wall_positions.add((new_wall_x, new_wall_y))

        # 캐릭터의 9방향 이동 이후에 벽이 움직인다 할지라도 충돌하지 않는 좌표민
        Q.extend([*(new_character_positions - new_wall_positions)])

    return 0


board, wall_positions = [], set()
for x in range(8):
    line = list(input())
    for y in range(8):
        if line[y] == "#":
            wall_positions.add((x, y))
    board.append(line)

start_character_x, start_character_y = 7, 0
Q = deque([(start_character_x, start_character_y)])
print(BFS(Q))
