from collections import deque

n, k = map(int, input().split())
left, right = deque(), deque(map(int, list(input())))

pop_count = 0
while right:
    num = right.popleft()
    while left and left[-1] < num and pop_count < k:
        left.pop()
        pop_count += 1
    left.append(num)

joined_deque = ''.join(map(str, list(left)))
print(joined_deque[:n-k] if pop_count < k else joined_deque)