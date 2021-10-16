from sys import setrecursionlimit
setrecursionlimit(1000000)

def dfs(x, y, mode):
    visited[x][y][mode] = True    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        newX, newY = x + dx, y + dy
        if (0 <= newX < n and 0 <= newY < n) and (not visited[newX][newY][mode]):
            if board[newX][newY][mode] == board[x][y][mode]:
                dfs(newX, newY, mode)

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[[False, False] for _ in range(n)] for _ in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] in "GR": board[x][y] += 'G'
        else: board[x][y] += 'B'

cnt = [0, 0]
for mode in range(2):
    for x in range(n): 
        for y in range(n):
            if not visited[x][y][mode]:
                cnt[mode] += 1
                dfs(x, y, mode)

print(cnt[0], cnt[1])