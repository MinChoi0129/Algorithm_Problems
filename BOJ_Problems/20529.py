from itertools import combinations as C
def getDistance(combi):
    dist = 0
    a, b, c = combi[0], combi[1], combi[2]

    # a vs b
    for i in range(4):
        if a[i] != b[i]:
            dist += 1

    # b vs c
    for i in range(4):
        if b[i] != c[i]:
            dist += 1

    # c vs a
    for i in range(4):
        if c[i] != a[i]:
            dist += 1

    return dist
    


for _ in range(int(input())):
    input()
    distances, combis = set(), set(C(input().split(), 3))
    for combi in combis:
        distances.add(getDistance(combi))
    print(min(distances))