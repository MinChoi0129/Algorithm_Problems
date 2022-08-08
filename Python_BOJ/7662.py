import heapq, sys
input = lambda : sys.stdin.readline().rstrip()
for _ in range(int(input())): # T
    Q_max, Q_min, had_been_deleted = [], [], dict()
    for i in range(int(input())): # K
        command = input().split()
        op, num = command[0], int(command[1])
        if op == 'I':
            heapq.heappush(Q_max, (-num, i))
            heapq.heappush(Q_min, (num, i))
            had_been_deleted[i] = False
        else:
            target_Q = Q_min if num == -1 else Q_max
            while target_Q and had_been_deleted[target_Q[0][1]]: heapq.heappop(target_Q)
            if target_Q: had_been_deleted[target_Q[0][1]] = True; heapq.heappop(target_Q)

    for Q in [Q_max, Q_min]:
        while Q and had_been_deleted[Q[0][1]]: heapq.heappop(Q)

    if Q_max: print(-Q_max[0][0], Q_min[0][0])   
    else: print("EMPTY")