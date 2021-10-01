import heapq, sys
input = lambda : sys.stdin.readline().rstrip()

problems = []

for _ in range(int(input())):
    number, level = map(int, input().split())
    heapq.heappush(problems, (level, number))

for _ in range(int(input())):
    get = input().split()
    if get[0] == 'add':
        number, level = int(get[1]), int(get[2])
        heapq.heappush(problems, (level, number))
    elif get[0] == 'recommend':
        x = int(get[1])
        
        if x == 1:
            print(heapq.nlargest(1, problems)[0][1])
        elif x == -1:
            print(heapq.nsmallest(1, problems)[0][1])
            
    elif get[0] == 'solved':
        solvedProblemNum = int(get[1])
        for i in range(len(problems)):
            if problems[i][1] == solvedProblemNum:
                problems.pop(i)
                break
        heapq.heapify(problems)