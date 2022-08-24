import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
stairs = [int(input()) for _ in range(n)]
stairs.insert(0, 0)

dp = [0] * 10001
dp[1] = stairs[1]

try:
    dp[2] = stairs[1] + stairs[2]
except:
    pass

try:
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
except:
    pass

for i in range(4, n + 1):
    dp[i] = max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])

print(dp[n])