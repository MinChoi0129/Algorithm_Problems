import sys
sys.setrecursionlimit(1000000)
input = lambda : sys.stdin.readline().rstrip()
def dfs(x, y):
    if [x, y] == [m-1, n-1]: return 1
    if dp[x][y] != -1: return dp[x][y]
    route = 0
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if 0 <= x+dx < m and 0 <= y+dy < n and board[x+dx][y+dy] < board[x][y]: route += dfs(x+dx, y+dy)
    dp[x][y] = route
    return route

m, n = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
print(dfs(0, 0))