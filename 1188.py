from math import gcd
n, m = map(int, input().split())
print(m - gcd(n, m))