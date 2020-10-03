import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

possible_combinations = list(combinations(cards, 3))
sums = []
for i in range(len(possible_combinations)):
    sums.append(sum(possible_combinations[i]))
max = 0
for i in range(len(sums)):
    if max < sums[i] <= m:
        max = sums[i]
print(max)