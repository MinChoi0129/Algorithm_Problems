n, m = map(int, input().split())
paper = [[*map(int, input().split())] for _ in range(n)]

blue_1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
blue_2 = [[0, 0], [1, 0], [2, 0], [3, 0]]
yellow = [[0, 0], [0, 1], [1, 0], [1, 1]]
orange_1 = [[0, 0], [1, 0], [2, 0], [2, 1]]
orange_2 = [[0, 1], [1, 1], [2, 1], [2, 0]]
orange_3 = [[0, 0], [0, 1], [1, 0], [2, 0]]
orange_4 = [[0, 0], [0, 1], [1, 1], [2, 1]]
orange_5 = [[0, 0], [0, 1], [0, 2], [1, 0]]
orange_6 = [[0, 0], [0, 1], [0, 2], [1, 2]]
orange_7 = [[0, 2], [1, 0], [1, 1], [1, 2]]
orange_8 = [[0, 0], [1, 0], [1, 1], [1, 2]]
green_1 = [[0, 0], [1, 0], [1, 1], [2, 1]]
green_2 = [[0, 1], [0, 2], [1, 0], [1, 1]]
green_3 = [[0, 1], [1, 0], [1, 1], [2, 0]]
green_4 = [[0, 0], [0, 1], [1, 1], [1, 2]]
purple_1 = [[0, 1], [1, 0], [1, 1], [1, 2]]
purple_2 = [[0, 1], [1, 0], [1, 1], [2, 1]]
purple_3 = [[0, 0], [1, 0], [2, 0], [1, 1]]
purple_4 = [[0, 0], [0, 1], [0, 2], [1, 1]]

tetrominos = [
    blue_1, blue_2, yellow, orange_1, orange_2, orange_3, orange_4, \
    orange_5, orange_6, orange_7, orange_8, green_1, green_2, green_3, \
    green_4, purple_1, purple_2, purple_3, purple_4, \
    ]

max_value = 0
for tetromino in tetrominos:
    for dx in range(n):
        for dy in range(m):
            tmp_score = 0
            for x, y in tetromino:
                try:
                    tmp_score += paper[x+dx][y+dy]
                except:
                    tmp_score = 0
                    break
            max_value = max(max_value, tmp_score)

print(max_value)