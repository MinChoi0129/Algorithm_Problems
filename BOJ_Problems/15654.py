from itertools import permutations as P
for case in P(r=[*map(int, input().split())][1], iterable=sorted(map(int, input().split()))):
    print(*case)