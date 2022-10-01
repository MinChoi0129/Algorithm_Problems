a, b, d = map(int, input().split())
is_primes = [None, False] + [True] * (b - 1)
for num in range(2, b + 1):
    for multiplier in range(2, b + 1):
        if num * multiplier > b: break
        is_primes[num * multiplier] = False

count = 0
for num in range(a, b + 1):
    if str(d) in str(num):
        if is_primes[num]: count += 1
        
print(count)