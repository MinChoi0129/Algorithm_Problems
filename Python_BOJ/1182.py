from itertools import combinations as C

n, s = map(int, input().split())
seq = [*map(int, input().split())]

combis = []
for r in range(1, len(seq) + 1):
    for combi in [*C(seq, r)]:
        combis.append(combi)

count = 0
for combi in combis:
    if sum(combi) == s:
        count += 1
print(count)