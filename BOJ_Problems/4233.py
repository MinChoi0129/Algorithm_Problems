def calculateConquerPowerWithMod(base, exp, mod):
    if exp <= 1: return base ** exp
    elif exp % 2 == 0: return ((calculateConquerPowerWithMod(base, exp // 2, mod) % mod) ** 2) % mod
    else: return base * (((calculateConquerPowerWithMod(base, (exp-1) // 2, mod) % mod) ** 2) % mod)

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

while True:
    p, a = map(int, input().split())
    if p == a == 0: break
    if isPrime(p): print("no")
    else: print("yes" if calculateConquerPowerWithMod(a, p, p) % p == a else "no")