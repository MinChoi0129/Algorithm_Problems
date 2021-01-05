from itertools import combinations

a, b = input(), input()

for i in range(min(len(a), len(b)), 0, -1):
    if list(set(combinations(a, i)) & set(combinations(b, i))):
        print(i)
        break