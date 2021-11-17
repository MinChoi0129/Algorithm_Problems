import heapq

for _ in range(int(input())): # T
    Q_max = []
    Q_min = []
    for _ in range(int(input())): # K
        command = input().split()
        op, num = command[0], int(command[1])
        if op == 'D':
            if not Q_max:
                continue            
            if num == 1: # 최댓값 삭제
                heapq.heappop(Q_max) # O(log(n))
                Q_min = []
                for num in Q_max: heapq.heappush(Q_min, -num)
            elif num == -1: # 최솟값 각제
                heapq.heappop(Q_min) # O(log(n))
                Q_max = []
                for num in Q_min: heapq.heappush(Q_max, -num)
        elif op == 'I':
            heapq.heappush(Q_max, -num) # O(nlog(n))
            heapq.heappush(Q_min, num) # O(nlog(n))

    if Q_max: print(-Q_max[0], Q_min[0])   
    else: print("EMPTY")