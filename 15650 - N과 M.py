import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
result = list(product(range(1, m + 1), range(1, n + 1)))

for i in range(len(result)):
    temp = list(result[i])
    for j in range(len(temp)):
        print(temp[j], end = " ")
    print("")