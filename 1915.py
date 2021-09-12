# import sys

# def check(square):
#     for line in square:
#         if '0' in line:
#             return [False, 0]
#     return [True, len(square)]

# n, m = map(int, sys.stdin.readline().rstrip().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# side = min(n, m)
# startX, startY = 0, 0
# maxSquare = 0
# while True:
#     endX, endY = startX + (side - 1), startY + (side - 1)
#     tempSquare = []
#     for x in range(startX, endX + 1):
#         yLine = []
#         for y in range(startY, endY + 1):
#             yLine.append(arr[x][y])
#         tempSquare.append(yLine)
    
#     result = check(tempSquare)
#     if result[0] == True:
#         maxSquare = result[1] ** 2
#         break
    
#     if endY < m - 1:
#         startY += 1
        
#     if endY == m - 1:
#         startY = 0
#         startX += 1
    
#     if endX == n - 1 and endY == m - 1 and side > 1:
#         side -= 1
#         startX = 0
    
#     if endX == n - 1 and endY == m - 1 and side == 1:
#         break
    
# print(maxSquare)

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

for line in arr:
    line.insert(0, 0)
arr.insert(0, list([0] * (m + 1)))

result = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == 1:
            arr[x][y] += min(arr[x - 1][y], arr[x][y - 1], arr[x - 1][y - 1])
        result = max(result, arr[x][y])

print(result ** 2)