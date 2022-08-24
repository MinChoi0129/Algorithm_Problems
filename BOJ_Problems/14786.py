import math
from decimal import *

a,b,c = [Decimal(i) for i in map(int,input().split())]
l,r,s = (c-b)/a, (c+b)/a, 50000
while l<r and s:
    x = (l+r)/2
    if x < (c - b * Decimal(math.sin(x)))/a:
        l = x + Decimal('0.0000001')
    else:
        r = x
    s -= 1

answer = str(x)
print(round(float(answer[:answer.find('.')+8]), 6))

'''
2초, 512MB
0 < B <= A <= 100,000
0 < C <= 100,000
오차허용 10^(-9)
'''
