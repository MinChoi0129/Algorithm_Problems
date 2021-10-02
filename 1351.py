n, p, q = map(int, input().split())

seq = [1]
floorDB = dict()

for i in range(1, n + 1):
    if i // p not in floorDB:
        floorDB[(i // p)] = i // p
    if i // q not in floorDB:
        floorDB[(i // q)] = i // q
    
for i in range(1, n + 1):
    seq.append(seq[floorDB[(i // p)]] + seq[floorDB[(i // q)]])

print(seq[n])