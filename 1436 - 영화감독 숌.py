import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
d = deque()
i = 666
while len(d) < n:
    if "666" in str(i):
        d.append(i)
    i += 1
print(d[-1])