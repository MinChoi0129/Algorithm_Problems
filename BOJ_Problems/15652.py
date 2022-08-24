import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().rstrip().split())
result = list(combinations_with_replacement([i for i in range(1, n + 1)], m))

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end = ' ')
    print("")