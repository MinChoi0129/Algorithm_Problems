from collections import deque


def tryInvading(enterance, w, h, board, my_keys):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_x, start_y = enterance

    Q = deque([(start_x, start_y)])
    visited = [[False] * w for _ in range(h)]
    visited[start_x][start_y] = True

    while Q:
        x, y = Q.popleft()
        for dx, dy in dxy:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < h and 0 <= new_y < w:
                value = board[new_x][new_y]
                if value != "*" and not visited[new_x][new_y]:
                    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and value in my_keys:
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))
                    elif value in "abcdefghijklmnopqrstuvwxyz":
                        my_keys.add(value)
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))
                    elif value == ".":
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))

    Q = deque([(start_x, start_y)])
    visited = [[False] * w for _ in range(h)]
    visited[start_x][start_y] = True

    number_of_documents = 0
    while Q:
        x, y = Q.popleft()
        if board[x][y] == "$":
            board[x][y] = "."
            number_of_documents += 1

        for dx, dy in dxy:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < h and 0 <= new_y < w:
                value = board[new_x][new_y]
                if value != "*" and not visited[new_x][new_y]:
                    if value in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and value in my_keys:
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))
                    elif value in "abcdefghijklmnopqrstuvwxyz":
                        my_keys.add(value)
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))
                    elif value == ".":
                        visited[new_x][new_y] = True
                        Q.append((new_x, new_y))

    return board, number_of_documents


for _ in range(int(input())):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    enterances, my_keys = set(), set()

    for letter in input():
        if letter != "0":
            my_keys.add(letter)

    for x in range(h):
        for y in range(w):
            if x in [0, h - 1] or y in [0, w - 1]:
                if (
                    board[x][y] in ".abcdefghijklmnopqrstuvwxyz"
                    or board[x][y] in my_keys
                ):
                    enterances.add((x, y))

    answer = 0
    for enterance in enterances:
        board, count = tryInvading(enterance, w, h, board, my_keys)
        answer += count

    print(answer)
