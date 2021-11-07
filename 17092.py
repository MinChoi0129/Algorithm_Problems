import sys
input = lambda : sys.stdin.readline().rstrip()
h, w, n = map(int, input().split())
if n == 0:
    print(h * w)
    for _ in range(9):
        print(0)
    sys.exit()


blacks = []
black_board_counts = {i : 0 for i in range(10)}

for _ in range(n):
    x, y = map(int, input().split())
    blacks.append((x-1, y-1))

for x in range(1, h - 1):
    for y in range(1, w - 1):
        count = 0
        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            if (x + dx, y + dy) in blacks:
                count += 1        
        black_board_counts[count] += 1
        
for count in black_board_counts.values():
    print(count)