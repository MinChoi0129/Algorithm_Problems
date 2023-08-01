from collections import deque

n = int(input())
lectures = sorted(tuple(map(int, input().split())) for _ in range(n))

if n == 1:
    print(1)
else:
    answer = 1
    Q = deque([lectures[0]])
    for next_start, next_end in lectures[1:]:
        current_start, current_end = Q.popleft()
        if current_end <= next_start:
            continue
        else:
            answer += 1
            Q.append((current_start, current_end))

    print(answer)