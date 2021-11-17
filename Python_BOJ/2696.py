import heapq

for _ in range(int(input())):
    m, left_heap, right_heap = int(input()), [], [] 

    answer = []
    arr = []
    while True:
        tmp = [*map(int, input().split())]
        arr += tmp
        if len(tmp) < 10:
            break

    for num in arr:
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -num)
        elif len(left_heap) > len(right_heap): # len(left) < len(right)
            heapq.heappush(right_heap, num)
        
        if right_heap and -left_heap[0] > right_heap[0]:
            wrong_left, wrong_right = heapq.heappop(left_heap), heapq.heappop(right_heap)
            heapq.heappush(left_heap, -wrong_right)
            heapq.heappush(right_heap, -wrong_left)
        
        if len(left_heap) > len(right_heap):
            answer.append(-left_heap[0])
    
    print(len(answer))
    for i in range(1, len(answer) + 1):
        print(answer[i - 1], end = " ")
        if i % 10 == 0:
            print()
    print()