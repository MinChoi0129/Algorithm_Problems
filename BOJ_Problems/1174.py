def raiseExceptionifBreakStatus():
    if len(answer) >= n : raise Exception(answer[n-1])
    elif answer[-1] == 9876543210: raise Exception(-1)

n = int(input())
answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

try:
    for element in answer:
        for i in range(int(str(element)[-1])):
            answer.append(int(str(element) + str(i)))
            raiseExceptionifBreakStatus()
except Exception as e: print(e)