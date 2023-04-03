from math import isqrt

a, b = map(int, input().split())
root_b = isqrt(b)
primes = []
is_primes = [False, False] + [True] * (root_b- 1)

for num in range(2, root_b + 1):
    if is_primes[num]:
        primes.append(num)
        for multiplier in range(2 * num, root_b + 1, num):
            is_primes[multiplier] = False

count = 0
for prime in primes:
    square = prime * prime
    while square <= b:
        if square >= a:
            count += 1
        square *= prime

print(count)