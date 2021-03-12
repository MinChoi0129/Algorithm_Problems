# 문제 : 11726 - 2xn 타일링
fibo = [0, 1]

for _ in range(int(input())):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1] % 10007)