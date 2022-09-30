result = 1
for num in range(2, int(input()) + 1):
    result *= num
    while str(result)[-1] == '0':
        result //= 10
    result %= 10000000000000000000
print(str(result)[-5:])