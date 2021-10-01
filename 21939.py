import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

problemsHeapQMinimum = []
problemsHeapQMaximum = []
problemSolved = dict()

for _ in range(int(input())):
    number, level = map(int, input().split())
    heapq.heappush(problemsHeapQMinimum, (level, number))
    heapq.heappush(problemsHeapQMaximum, (-level, -number))
    problemSolved[number] = False

for _ in range(int(input())):
    get = input().split()
    if get[0] == 'add':
        number, level = int(get[1]), int(get[2])
        while problemSolved[problemsHeapQMinimum[0][1]]: # 레벨이 가장 낮은 문제를 푼게 하나라도 있으면
            heapq.heappop(problemsHeapQMinimum)
        while problemSolved[-problemsHeapQMaximum[0][1]]: # 레벨이 가장 높은 문제를 푼게 하나라도 있으면
            heapq.heappop(problemsHeapQMaximum)

        heapq.heappush(problemsHeapQMinimum, (level, number))
        heapq.heappush(problemsHeapQMaximum, (-level, -number))
        problemSolved[number] = False
        

    elif get[0] == 'recommend':
        
        if get[1] == '1': # hard
            while problemSolved[-problemsHeapQMaximum[0][1]]: # 레벨이 가장 높은 문제를 푼게 하나라도 있으면
                heapq.heappop(problemsHeapQMaximum)
            print(-problemsHeapQMaximum[0][1])
        else: # easy
            while problemSolved[problemsHeapQMinimum[0][1]]: # 레벨이 가장 낮은 문제를 푼게 하나라도 있으면
                heapq.heappop(problemsHeapQMinimum)
            print(problemsHeapQMinimum[0][1])
    elif get[0] == 'solved':
        problemSolved[int(get[1])] = True