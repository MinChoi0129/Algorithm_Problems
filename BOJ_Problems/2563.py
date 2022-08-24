board = [[0] * 100 for _ in range(100)]
paper = int(input())

for _ in range(paper):
    x_0, y_0 = map(int, input().split())
    for x in range(10):
        for y in range(10):
            board[x_0 - 1 + x][y_0 - 1 + y] = 1
            
            
area = 0
for x in board:
    for y in x:
        if y == 1:
            area += 1
            
print(area)