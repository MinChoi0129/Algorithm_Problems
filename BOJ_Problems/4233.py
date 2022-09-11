def caulcateConquerPowerWithMod(base, exp, mod):
    if exp == 0: return 1
    elif exp == 1: return base

    if exp % 2 == 0:
        value = caulcateConquerPowerWithMod(base, exp // 2, mod)
        return ((value % mod) ** 2) % mod
    else:
        value = caulcateConquerPowerWithMod(base, (exp-1) // 2, mod)
        return base * (((value % mod) ** 2) % mod)

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

while True:
    p, a = map(int, input().split())
    if p == a == 0: break
    if isPrime(p): print("no")
    else: print("yes" if caulcateConquerPowerWithMod(base = a, exp = p, mod = p) % p == a % p else "no")