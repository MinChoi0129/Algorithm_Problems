a, b = map(int, input().split())
MAX_SIZE = 10 ** 7
is_primes = [False, False] + [True] * (MAX_SIZE - 1)

for i in range(2, MAX_SIZE + 1):
    if is_primes[i]:
        for j in range(2*i, MAX_SIZE + 1, i):
            is_primes[j] = False

count = 0
for num in range(2, MAX_SIZE + 1):
    if is_primes[num]:
        n = 2
        while True:
            target = num ** n
            if target > b: break
            if a <= target <= b:
                count += 1
print(count)