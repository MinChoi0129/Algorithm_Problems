n, a, b = int(input()), 1, 3
if n == 1: print(1)
else:
    for _ in range(n-2):
        a, b = b % 10007, ((2 * (a % 10007)) % 10007 + b % 10007) % 10007
    print(b % 10007)