def solve(mode, n):
    if mode == 'A': return (n-1)**2//4 if n%2 == 1 else (n**2-2*n)//4
    elif mode == 'B':
        # 약수 배열 생성
        divisors = [False]*n + [True]
        for num in range(1, n//2 + 1):
            if n % num == 0: divisors[num] = True
        # 풀이
        count = 0
        for i in range(1, len(divisors)):
            if divisors[i]: # 시간초과 방지
                for j in range(i, len(divisors)):
                    if divisors[j]: # 시간초과 방지
                        if i+j > n: break # 인덱스 초과 방지
                        if divisors[i+j]: count += 1
        return count
    elif mode == 'C':
        # 소수 배열 생성
        is_primes = [False, False] + [True] * (n-1)
        for i in range(2, int(n ** 0.5) + 1):
            if is_primes[i]:
                for j in range(2*i, n + 1, i):
                    is_primes[j] = False
        # 풀이
        return [is_primes[i] and is_primes[i+2] for i in range(2, n-1)].count(True)

n = int(input())
for mode in 'ABC':
    print(solve(mode, n))