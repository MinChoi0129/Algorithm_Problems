import sys
import math
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

pft_sqrs = []

def is_pft_sqrs(num):
    if num == int((math.sqrt(num))) ** 2:
        return True
    return False

for num in range(m, n + 1):
    if is_pft_sqrs(num):
        pft_sqrs.append(num)

if len(pft_sqrs) == 0:
    print(-1)
else:
    print(sum(pft_sqrs))
    print(min(pft_sqrs))