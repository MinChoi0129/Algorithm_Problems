s, k = map(int, input().split())
splitted_numbers = [s // k for _ in range(k)]
for i in range(s % k): splitted_numbers[i] += 1
result = 1
for num in splitted_numbers: result *= num
print(result)