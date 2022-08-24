from collections import deque

n = int(input())
Q, visited = deque([(n, [n])]), [False] * (n+1)

while Q:
    present_number, history = Q.popleft()
    if present_number == 1:
        print(len(history)-1); print(*history)
        break
    
    if not visited[present_number]:
        visited[present_number] = True
        if present_number % 3 == 0: Q.append((present_number//3, history + [present_number//3]))
        if present_number % 2 == 0: Q.append((present_number//2, history + [present_number//2]))
        if present_number -1 > 0: Q.append((present_number-1, history + [present_number-1]))