n = int(input())
is_primes = [False, False] + [True] * (n - 1) # 0 <= <= n 까지 모든 수의 소수 여부

for num_idx in range(n + 1):
    if is_primes[num_idx]:
        for i in range(2 * num_idx, n + 1, num_idx):
            is_primes[i] = False

primes = [i for i in range(len(is_primes)) if is_primes[i]]

p1, p2, count = 0, 0, 0
while p2 < len(primes):
    tmp = sum(primes[p1 : p2 + 1])
    if tmp == n: count, p1 = count + 1, p1 + 1
    elif tmp < n: p2 += 1
    else: p1 += 1

print(count)