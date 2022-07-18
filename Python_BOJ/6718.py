# numbers = []
# while True:
#     number = int(input())
#     if number == 0: break
#     else: numbers.append(number)

# def getPrimesListTo(max_num):
#     isPrimes = [False, False] + [True for _ in range(max_num - 2)]
#     for num in range(2, max_num):
#         multiplier = 2
#         while num * multiplier < max_num:
#             isPrimes[num * multiplier] = False
#             multiplier += 1

#     return [i for i in range(len(isPrimes)) if isPrimes[i]]

# # primes = getPrimesListTo(max(numbers))
# # for num in numbers:
# #     p1, p2, possible_pairs_count = 0, 0, 0
    
# #     while p1 <= len(primes) - 1:
# #         if primes[p1] + primes[p2] == num: possible_pairs_count += 1
# #         p2 += 1
# #         if p2 > len(primes) - 1:
# #             p1 += 1
# #             if p1 > len(primes) - 1: break
# #             p2 = p1
# #         if primes[p2] >= num:
# #             p1 += 1
# #             p2 = p1
# #         if primes[p1] >= num: break
# #     print(possible_pairs_count)

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

numbers = []
while True:
    number = int(input())
    if number == 0: break
    else: numbers.append(number)

primes = [False] * max(numbers)
for i in range(2, len(primes)):
    if isPrime(i): primes[i] = True

for num in numbers:
    count = 0
    for i in range(2, num // 2 + 1):
        if primes[i] and primes[num - i]:
            count += 1
    print(count)
                
