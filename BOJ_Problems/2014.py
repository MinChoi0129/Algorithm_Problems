import heapq

k, n = map(int, input().split())
primes = [*map(int, input().split())]

result = list(primes)
for _ in range(n - 1):
    root = heapq.heappop(result)
    for prime in primes:
        heapq.heappush(result, prime * root)
        if root % prime == 0:
            break
print(result[0])