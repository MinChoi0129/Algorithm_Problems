p = 1000000007
factorials = [1] * 4000001
for i in range(1, 4000000 + 1):
    factorials[i] = (factorials[i-1] * i) % p

for _ in range(int(input())):
    n, k = map(int, input().split())
    # nCk % p = n! % p * (k! * (n-k)!)^(p-2)%p
    a = factorials[n]
    b = pow(factorials[n-k] * factorials[k], p-2, p)
    print((a * b) % p)