import math

def alpha(x, y):
    dist = y - x
    if dist <= 3:
        return dist
    else:
        n = int(math.sqrt(dist))
        if dist == n ** 2:
            return 2 * n - 1
        elif n ** 2 < dist <= n ** 2 + n:
            return 2 * n
        else:
            return 2 * n + 1

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    print(alpha(x, y))