test_cases, primes, primes2 = [], [], []

def goldbach_conjecture(num):
    for a in primes:
        for b in primes2:
            if a > b:
                print("Goldbach's conjecture is wrong.")
                return
            else:
                if num == a + b:
                    print("%d = %d + %d" % (num, a, b))
                    return

def setOddPrimes(max_num):
    global primes, primes2
    for num in range(3, max_num + 1, 2): # 홀수only, 2는 문제에서 제외시킴
        if isPrime(num):
            primes.append(num)
    primes2 = list(reversed(primes))

def isPrime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

while True:
    get = int(input())
    if get == 0:
        break
    else:
        test_cases.append(get)

setOddPrimes(max(test_cases))
for case in test_cases:
    goldbach_conjecture(case)
