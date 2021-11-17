import sys, heapq

input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    tmp = []
    for _ in range(int(input())):
        school, num = input().split()
        heapq.heappush(tmp, (-int(num), school))
    print(tmp[0][1])