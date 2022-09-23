test_case = [int(input()) for _ in range(int(input()))]

MAX_SIZE = max(test_case)

f, g = [None] + [1] * MAX_SIZE, [0] * (MAX_SIZE + 1)

for base in range(2, MAX_SIZE + 1):
    for multiplier in range(1, MAX_SIZE + 1):
        idx = base * multiplier
        if idx > MAX_SIZE: break
        f[idx] += base

for idx in range(1, MAX_SIZE + 1): g[idx] += g[idx-1] + f[idx]
for case in test_case: print(g[case])