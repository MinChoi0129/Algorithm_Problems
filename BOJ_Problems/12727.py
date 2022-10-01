import decimal
decimal.getcontext().prec = 2000000000
from math import sqrt

base = decimal.Decimal('3') + decimal.Decimal(sqrt(5))

for i in range(int(input())):
    result = 1
    for _ in range(int(input())): result *= base
    result = int(str(int(result))[-3:])
    print("Case #%d: %03d" % (i + 1, result))