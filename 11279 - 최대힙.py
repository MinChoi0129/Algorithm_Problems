import sys
from heapq import *
input = lambda : sys.stdin.readline().rstrip()

myList = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        try:
            print(-1 * heappop(myList))
        except:
            print(0)
    else:
        heappush(myList, (-num))