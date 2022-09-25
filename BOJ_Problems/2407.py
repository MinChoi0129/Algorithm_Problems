from math import factorial as fact
def nCm(n, m): return fact(n) // (fact(m) * fact(n-m))
print(nCm(*map(int, input().split())))