n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in range(m):
        dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x-1][y-1] - dp[x-2][y-1] - dp[x-1][y-2] + dp[x-2][y-2])