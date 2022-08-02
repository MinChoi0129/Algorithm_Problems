n = int(input())

if n < 8: print(-1)
else:
    primes = [False, False] + [True] * (n - 1)
    for num in range(2, n+1):
        for non_prime_num in range(2*num, n+1, num):
            primes[non_prime_num] = False
    
    result = [2, 2] if n % 2 == 0 else [2, 3]
    n -= sum(result)
    for num in range(2, n+1):
        if primes[num] and primes[n - num]:
            result.append(num)
            result.append(n - num)
            break
    for num in result: print(num, end = " ")