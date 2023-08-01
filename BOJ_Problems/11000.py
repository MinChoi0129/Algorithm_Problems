import heapq

n = int(input())
lectures = sorted(list(map(int, input().split())) for _ in range(n))
first_start, first_end = lectures[0]

heap = [first_end]

for next_start, next_end in lectures[1:]:
    current_end = heap[0]
    if current_end <= next_start:
        heapq.heappop(heap)
    heapq.heappush(heap, next_end)

print(len(heap))
