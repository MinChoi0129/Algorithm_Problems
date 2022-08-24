def printStrangePrimes(num):
    if len(num) == n: print(num); return
    for e in "1379":
        new_num = num+e
        if isPrime(int(new_num)): printStrangePrimes(new_num)

def isPrime(num):
    if num == 1: return False
    for i in range(2, int(int(num) ** 0.5) + 1):
        if num % i == 0: return False
    return True

n = int(input())
for f in "2357": printStrangePrimes(f)