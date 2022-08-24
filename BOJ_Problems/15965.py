def getPrimesListTo(max_num):
    isPrimes = [False, False] + [True for _ in range(max_num - 2)]
    for i in range(2, int(max_num ** 0.5) + 1):
        for j in range(2 * i, max_num, i):
            isPrimes[j] = False
    return [i for i in range(len(isPrimes)) if isPrimes[i]]

print(getPrimesListTo(10000000)[int(input()) - 1])