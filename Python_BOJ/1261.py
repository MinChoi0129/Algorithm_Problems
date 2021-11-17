from collections import deque

m, n = map(int, input().split())
maze = [list(input()) for _ in range(n)]

Q = deque()
Q.append([0, 0])

answer = [[-1] * m for _ in range(n)]
answer[0][0] = 0

while Q:
    x, y = Q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우 탐색
        newX, newY = x + dx, y + dy
        if 0 <= newX < n and 0 <= newY < m: # 범위 내
            if answer[newX][newY] == -1: # 미방문
                if maze[newX][newY] == '0':
                    Q.appendleft([newX, newY])
                    answer[newX][newY] = answer[x][y] # 벽 안부쉈으니 +0
                elif maze[newX][newY] == '1':
                    Q.append([newX, newY])
                    answer[newX][newY] = answer[x][y] + 1 # +1의 의미 : 벽부수기 count 증가

print(answer[n-1][m-1])