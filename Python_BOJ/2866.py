# import sys
# input = lambda : sys.stdin.readline().rstrip()
# r, c = map(int, input().split())
# count = 0

# board = [input() for _ in range(r)]

# while count < r:
#     dictionary = dict()
#     for y in range(c):
#         tmp = ""
#         for x in range(count + 1, r): tmp += board[x][y]
#         if tmp in dictionary: dictionary[tmp] += 1
#         else: dictionary[tmp] = 1

#     for val in dictionary.values():
#         if val != 1:
#             print(count)
#             sys.exit()
#     count += 1