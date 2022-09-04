small, big = map(int, input().split())
size = big - small + 1
is_square_number = [False] * size

for num in range(2, int(big ** 0.5) + 1):
    square_num = num ** 2
    start_num = square_num * (1 + ((small-1) // square_num))
    for multiplied_square_num in range(start_num, big + 1, square_num):
        is_square_number[multiplied_square_num - small] = True

print(is_square_number.count(False))