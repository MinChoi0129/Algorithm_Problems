import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().rstrip().split())
result = list(permutations(range(1, n + 1), m))

for i in range(len(result)):
    temp = list(result[i])
    for j in range(len(temp)):
        print(temp[j], end = " ")
    print("")