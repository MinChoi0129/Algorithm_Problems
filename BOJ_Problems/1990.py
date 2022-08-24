def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

a, b = map(int, input().split())
if b > 10000000: b = 10000000
for i in range(a, b + 1):
    if str(i) == str(i)[::-1] and isPrime(i):
        print(i)
print(-1)