def getFourPrimesForNum(num):
    global primes

    num -= 4
    if num % 2 == 0: # 4 + 짝 or 5 + 홀, 에서 아무조합이나 가능
        if num == 4: return "2 2 2 2"
        else:
            size = len(primes)
            for i in range(size):
                for j in range(i, size):
                    if primes[i] + primes[j] == num:
                        return "2 2 " + str(primes[i]) + " " + str(primes[j])

    else: # 4 + 홀
        num -= 2
        return "2 2 2 " + str(num)

is_primes = [False, False] + [True] * 100000000
for i in range(2, len(is_primes)):
    for j in range(i+i, len(is_primes), i):
        is_primes[j] = False
        
while True:
    try:
        num = int(input())
        if num < 8: print("Impossible.")
        print(getFourPrimesForNum(num))
    except: break