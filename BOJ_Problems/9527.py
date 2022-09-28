a, b = map(int, input().split())
result = 0
for num in range(a, b + 1):
    print(num, bin(num)[2:].count('1'))
print(result)