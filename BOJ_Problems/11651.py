import sys
n = int(input())

point = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x, y])
for i in range(n):
    point[i][0], point[i][1] = point[i][1], point[i][0]
    
point.sort()

for i in range(n):
    print("%d %d" % (point[i][1], point[i][0]))