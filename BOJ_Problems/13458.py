n = int(input())
examinations = [*map(int, input().split())]
b, c = map(int, input().split())
for i in range(len(examinations)):
    examinations[i] -= b
    if examinations[i] < 0: examinations[i] = 0
    if examinations[i] % c == 0: n += examinations[i] // c
    else: n += examinations[i] // c + 1

print(n)