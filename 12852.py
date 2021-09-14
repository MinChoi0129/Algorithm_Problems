n = int(input())
dp = [0] * 1000001
dp[2] = 1
myN = n
process = [n]

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + 1 # 1을 빼는 연산

    if i % 3 == 0:
        if dp[i] >= dp[i // 3] + 1:
            process.append(myN // 3)
            myN //= 3
            dp[i] = dp[i // 3] + 1
        else:
            process.append(myN - 1)
            myN -= 1

    
    if i % 2 == 0:
        if dp[i] >= dp[i // 2] + 1:
            process.append(myN // 2)
            myN //= 2
            dp[i] = dp[i // 2] + 1
        else:
            process.append(myN - 1)
            myN -= 1

for i in range(len(process)):
    print(process[i], end = " -> ") 
print(dp[n])