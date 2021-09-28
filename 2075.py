import heapq, sys
N = int(input())
heap = []
for _ in range(N):
    nums = list(map(int,sys.stdin.readline().rstrip().split()))

    if not heap: 
        for num in nums:
            heapq.heappush(heap,num)
    else:
        for num in nums:
            if heap[0] < num: # heapq에서 idx 0은 root node로서 최솟값임
                heapq.heappushpop(heap, num)
print(heap[0])