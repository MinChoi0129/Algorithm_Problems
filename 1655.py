import heapq

n, left_heap, right_heap = int(input()), [], [] 

answers = []
for _ in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else: # len(left) < len(right)
        heapq.heappush(right_heap, num)
    
    if right_heap and -left_heap[0] > right_heap[0]:
        wrong_left = -heapq.heappop(left_heap) # >=0, left_heap의 최댓값
        wrong_right = heapq.heappop(right_heap) # >=0, right_heap의 최솟값
        
        heapq.heappush(left_heap, -wrong_right)
        heapq.heappush(right_heap, wrong_left)
    
    answers.append(-left_heap[0])
    
for answer in answers:
    print(answer)