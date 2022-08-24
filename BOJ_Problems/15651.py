import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())

result = list(product(range(1, n + 1), repeat = m))
for i in range(n ** m):
    for j in range(m):
        print(result[i][j], end = ' ')
    print("")