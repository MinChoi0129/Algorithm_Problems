from itertools import permutations as P

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    perms = set()
    for size in range(1, len(numbers) + 1):
        for i in P(numbers, size):
            perms.add(int(''.join(i)))
    
    count = 0
    for num in perms:
        if isPrime(num):
            count += 1
    return count

print(solution(input()))