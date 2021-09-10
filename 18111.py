import sys

ground = []
ground_data = dict()
TIME_BY_DIG, TIME_BY_PUT = 2, 1
min_time, that_height = 128000000, 0


def try_to_make(ground_data, trying_height):
    time = 0

    for data in ground_data.items():
        if data[0] < trying_height:
            time += TIME_BY_PUT * data[1] * (trying_height - data[0])
        elif data[0] > trying_height:
            time += TIME_BY_DIG * data[1] * (data[0] - trying_height)

    return time, trying_height


n, m, b = map(int, sys.stdin.readline().rstrip().split())

for i in range(n):
    ground += map(int, sys.stdin.readline().rstrip().split())

for i in ground:
    if i not in ground_data:
        ground_data[i] = 1
    else:
        ground_data[i] += 1

existing_blocks = sum(ground) + b

for height in range(257):

    if n * m * height > existing_blocks:
        continue

    temp_time, temp_that_height = try_to_make(ground_data, height)
    if temp_time < min_time:
        min_time, that_height = temp_time, temp_that_height
    elif temp_time == min_time:
        if that_height < temp_that_height:
            min_time, that_height = temp_time, temp_that_height

print(min_time, that_height)