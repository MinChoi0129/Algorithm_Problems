from collections import deque

dxy = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def BFS(Q, wall_positions):
    while Q:
        for _ in range(len(Q)):
            x, y = Q.popleft()
            if (x, y) in wall_positions:
                continue
            if (x, y) == (0, 7):
                return 1
            
            for dx, dy in dxy:
                new_x, new_y = x + dx, y + dy
                if (    0 <= new_x < 8 
                    and 0 <= new_y < 8
                    and (new_x, new_y) not in wall_positions
                ):
                    Q.append((new_x, new_y))

        wall_positions = {(x+1, y) for x, y in wall_positions if x+1 < 8}

    return 0

wall_positions = set()
for x in range(8):
    line = list(input())
    for y in range(8):
        if line[y] == "#":
            wall_positions.add((x, y))

x, y = 7, 0
Q = deque([(x, y)])
print(BFS(Q, wall_positions))
