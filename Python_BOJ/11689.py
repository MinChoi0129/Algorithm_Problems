n = int(input())
answer = n
for num in range(2, int(n**0.5)+1):
    if n % num == 0:
        while not n % num: n //= num
        answer *= ((num - 1) / num)
print(int(answer if n == 1 else answer * ((n - 1) / n)))