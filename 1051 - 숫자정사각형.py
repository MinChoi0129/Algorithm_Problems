import sys

def find_square(size):
    for h in range(N - size + 1):
        for w in range(M - size + 1):
            if square_check(h, w):
                print(size ** 2)
                return "STOP"
    return "NEXT"

def square_check(h, w):
    global rect
    lu = rect[h][w]
    ru = rect[h][w + size - 1]
    ld = rect[h + size - 1][w]
    rd = rect[h + size - 1][w + size - 1]
    if lu == ru == ld == rd:
        return True
    return False

N, M = map(int, sys.stdin.readline().rstrip().split())
short_side_length = min(N, M)

rect = []

for _ in range(N):
    rect.append(sys.stdin.readline().rstrip())


for size in range(short_side_length, 0, -1):
    if find_square(size) == "STOP":
        break