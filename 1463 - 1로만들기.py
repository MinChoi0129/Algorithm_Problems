n = int(input())
dp = [0] * 1000001
dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 1 # 1을 빼는 연산
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
print(dp[n])