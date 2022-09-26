from itertools import permutations as P
for case in sorted(set(P(r=[*map(int, input().split())][1], iterable=map(int, input().split())))):
    print(*case)