n, k = map(int, input().split())
dp = [[1] * (n+1) for _ in range(k+1)]

try:
    for y in range(1, n+1):
        dp[2][y] = y+1
    for x in range(3, k+1):
        for y in range(1, n+1):
            dp[x][y] = (dp[x][y-1] + dp[x-1][y]) % 1000000000
except: pass
finally: print(dp[k][n])