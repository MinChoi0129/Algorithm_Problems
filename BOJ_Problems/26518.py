b, c, a1, a2 = map(int, input().split())
for _ in range(100):
    a3 = b * a2 + c * a1
    a4 = b * a3 + c * a2
    a1, a2 = a3, a4

print(round((a2 / a1), 9))