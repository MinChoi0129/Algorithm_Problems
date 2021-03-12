# 문제 : 1026 - 보물
tot, n, a, b = \
    0, int(input()), \
    sorted(list(map(int, input().split())), reverse = True), \
    sorted(list(map(int, input().split())))

for i in range(n):
    tot += a[i] * b[i]

print(tot)