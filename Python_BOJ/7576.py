import collections, sys
m, n = map(int, input().split())
farm = [[*map(int, input().split())] for _ in range(n)]
Q = collections.deque([(x, y) for x in range(n) for y in range(m) if farm[x][y] == 1])

while Q:
    x, y = Q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if (0 <= new_x < n and 0 <= new_y < m) and not farm[new_x][new_y]:
            farm[new_x][new_y] = farm[x][y] + 1
            Q.append((new_x, new_y))
        
answer = -1
for line in farm:
    for cell in line:
        if not cell: print(-1); sys.exit(0)
    answer = max(answer, max(line)-1)
print(answer)