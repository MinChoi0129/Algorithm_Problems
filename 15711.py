MAX_SIZE = 2 * (10 ** 6)
is_prime = [False, False] + [True] * (MAX_SIZE - 1)
primes = []

for num_idx in range(2, MAX_SIZE + 1):
    if is_prime[num_idx]:
        primes.append(num_idx)
        for i in range(2 * num_idx, MAX_SIZE + 1, num_idx):
            is_prime[i] = False

def isPrime(num):
    if num > MAX_SIZE:
        for prime in primes:
            if num % prime == 0:
                return False
        return True
    else:
        return is_prime[num]

for _ in range(int(input())):
    a_plus_b = sum(map(int, input().split()))
    
    if a_plus_b in [2, 3]: # 2 : 1 + 1, 3 : 2 + 1 -> 소수를 사용하지 않음
        print("NO")
    
    elif a_plus_b % 2 == 0: # 골드바흐의 추측 : 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
        print("YES")
    
    else: # 홀수.   //   홀수(인 소수) = 홀수(인 소수) + 짝수(인 소수 == 2)
        if isPrime(a_plus_b - 2):
            print("YES")
        else:
            print("NO")