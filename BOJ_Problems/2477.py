k = int(input())
lines = [[*map(int, input().split())] for _ in range(6)]

max_height, max_height_idx = 0, 0
max_width, max_width_idx = 0, 0
for i in range(6):
    direction, length = lines[i]
    if direction in [1, 2] and max_width < length:
        max_width = length
        max_width_idx = i
    elif direction in [3, 4] and max_height < length:
        max_height = length
        max_height_idx = i

small_farm_height = abs(lines[(max_width_idx - 1) % 6][1] - lines[(max_width_idx + 1) % 6][1])
small_farm_width = abs(lines[(max_height_idx - 1) % 6][1] - lines[(max_height_idx + 1) % 6][1])
area = max_width * max_height - small_farm_width * small_farm_height
print(k * area)