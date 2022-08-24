# N = int(input())
#
# coordinates = []
#
# for i in range(N):
#     x, y = map(int, input().split())
#     coordinates.append((x, y))
#
# for i in range(N, 0, -1):
#     max_x_index = 0
#     for j in range(i):
#         if coordinates[j][0] > coordinates[max_x_index][0]:
#             max_x_index = j
#     coordinates[0], coordinates[i - N - 1] = coordinates[i - N - 1], coordinates[0]
#
#
# y정렬 실패
#
# print(sorted_coordinates)


import sys
n = int(input())

point = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    point.append([x, y])
point.sort()

for i in range(n):
    print("%d %d" % (point[i][0], point[i][1]))