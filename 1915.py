def check(square):
    for line in square:
        if '0' in line:
            return [False, 0]
    return [True, len(square)]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

side = min(n, m)
startX, startY = 0, 0
maxSquare = 0
while True:
    endX, endY = startX + (side - 1), startY + (side - 1)
    tempSquare = []
    for x in range(startX, endX + 1):
        yLine = []
        for y in range(startY, endY + 1):
            yLine.append(arr[x][y])
        tempSquare.append(yLine)
    
    result = check(tempSquare)
    if result[0] == True:
        maxSquare = result[1] ** 2
        break
    
    if endY < m - 1:
        startY += 1
        
    if endY == m - 1:
        startY = 0
        startX += 1
    
    if endX == n - 1 and endY == m - 1 and side > 1:
        side -= 1
        startX = 0
    
    if endX == n - 1 and endY == m - 1 and side == 1:
        break
    
print(maxSquare)    