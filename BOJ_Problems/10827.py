from decimal import Decimal, getcontext
getcontext().prec = 99*100+9
a, b = input().split()
print("{0:f}".format(Decimal(a) ** int(b)))