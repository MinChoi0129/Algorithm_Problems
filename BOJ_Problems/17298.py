from collections import deque

n = int(input())
numbers = [*map(int, input().split())]
stack, result = deque(), deque()

for i in range(len(numbers) - 1, -1, -1):
    if not stack:
        result.appendleft(-1)
        stack.append(numbers[i])
    else:
        while stack:
            if stack[-1] <= numbers[i]:
                stack.pop()
                if not stack:
                    result.appendleft(-1)
            elif stack[-1] > numbers[i]:
                result.appendleft(stack[-1])
                break
        stack.append(numbers[i])

for i in result:
    print(i, end = " ")