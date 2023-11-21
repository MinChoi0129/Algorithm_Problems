import bisect

d, n = map(int, input().split())
oven_diameters = [*map(int, input().split())]
pizza_diameters = [*map(int, input().split())]

for i in range(1, d):
    oven_diameters[i] = min(oven_diameters[i], oven_diameters[i-1])

