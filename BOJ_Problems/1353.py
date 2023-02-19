"""c만 통과됨."""
# import math, decimal
# decimal.getcontext().prec = 100
# e = decimal.Decimal('2.7182818459045')

# def solution():
#     s, p = map(decimal.Decimal, input().split())
#     if s == p:
#         return 1

#     if decimal.Decimal(math.pow(e, s / e)) < p:
#         return -1

#     prv = decimal.Decimal('-1');
#     i = 2;
#     while True:
#         cur = decimal.Decimal(math.pow(s / i, i))
#         if (prv > cur):
#             return -1
#         if (cur >= p):
#             return i
#         prv = cur
#         i += 1

# print(solution())