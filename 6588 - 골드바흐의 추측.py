import sys

def goldbach_conjecture(get):
    global size
    for number in range(3, int(size ** 0.5) + 1):
        a, b = number, get - number
        if a >= 3 and b >= 3:
            if primes[a] and primes[b]:
                if a + b == get:
                    print("%d = %d + %d" % (get, a, b))
                    return
    print("Goldbach's conjecture is wrong.")
    return

def setPrimes(size):
    size += 1
    numbers = [True] * size

    for i in range(2, int(size ** 0.5) + 1): # sqrt
        if numbers[i]:
            for j in range(2 * i, size, i):
                ''' start = 남은 소수 중 첫번째는 소수이므로 두번째부터
                end = size - 1 = 1000000 까지
                step = i의 배수들을 False로 정의한다.
                
                -  합성수를 활용한 에라토스테네스의 체  -  '''
                numbers[j] = False

    return numbers

size = 1000000
primes = setPrimes(size)

while True:
    get = int(sys.stdin.readline().rstrip())
    if get == 0: break
    else: goldbach_conjecture(get)
