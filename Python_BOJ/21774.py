from sys import stdin
from bisect import bisect_left as BL
from bisect import bisect_right as BR

input = lambda : stdin.readline().rstrip()

n, q = map(int, input().split())
logs = {i + 1 : [] for i in range(6)}

for _ in range(n):
    timeline, level = input().split("#")
    logs[int(level)].append(timeline)

for _ in range(q):
    start, end, level = input().split("#")
    count = 0
    for lv in range(int(level), 7):
        if logs[lv]:
            count += BR(logs[lv], end) - BL(logs[lv], start)            
    print(count)