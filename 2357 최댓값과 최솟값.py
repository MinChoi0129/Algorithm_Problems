import sys

num = []

n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    num.append(int(sys.stdin.readline()))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    new_num = []
    for i in range(a - 1, b):
        new_num.append(num[i])
    print("%d %d" % (min(new_num), max(new_num)))