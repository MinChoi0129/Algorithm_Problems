import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

heap = []

for _ in range(int(input())):
    get = int(input())
    if get == 0:
        if not heap: print(0)
        else: print(heapq.heappop(heap)[1])
    else: heapq.heappush(heap, (abs(get), get))