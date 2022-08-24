from collections import deque
import sys

d = deque()
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    order = sys.stdin.readline().rstrip().split()
    a = order[0]
    if a == "push":
        d.append(order[1])
    elif a == "pop":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif a == "size":
        print(len(d))
    elif a == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif a == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)