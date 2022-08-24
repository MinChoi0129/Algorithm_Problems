n = int(input())
points = [[*map(int, input().split())] for _ in range(n)]
points.append(points[0])

a, b = 0, 0
for i in range(n):
    a += points[i][0] * points[i + 1][1]
    b += points[i + 1][0] * points[i][1]

print(round(abs(a - b) * 0.5, 1))