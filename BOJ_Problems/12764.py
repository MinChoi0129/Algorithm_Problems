from sys import stdin as sin
from collections import deque
input = lambda : sin.readline().rstrip()
computers = [0, 0] * 100000
users = deque([[*map(int, input().split())] for _ in range(int(input()))])
users.sort()

while users:
    start, end = users.popleft()
    